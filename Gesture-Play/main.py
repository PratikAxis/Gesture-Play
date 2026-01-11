import sys
import os

# This tells Python to look inside the 'Gesture-Play' folder for modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'Gesture-Play'))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import cv2
from src.hand_tracking import HandTracker
from src.gesture_logic import detect_gesture
from src.game_controller import GameController

def main():
    tracker = HandTracker()
    controller = GameController()

    while True:
        frame, landmarks = tracker.get_frame_and_landmarks()
        gesture = detect_gesture(landmarks)

        print("Gesture:", gesture)  # Debug output
        controller.perform_action(gesture)

        # Optional HUD overlay
        cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Gesture Play", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    tracker.release()

if __name__ == "__main__":
    main()