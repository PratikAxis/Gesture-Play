import numpy as np

def finger_is_open(landmarks, tip, pip, wrist=0, threshold=0.02):
    """Returns True if the finger tip is higher than the joint (PIP)"""
    return landmarks[tip].y < landmarks[pip].y - threshold

def detect_gesture(landmarks):
    if landmarks is None:
        return "IDLE"

    index_open = finger_is_open(landmarks, 8, 6)
    middle_open = finger_is_open(landmarks, 12, 10)
    ring_open = finger_is_open(landmarks, 16, 14)
    pinky_open = finger_is_open(landmarks, 20, 18)

    fingers_open = [index_open, middle_open, ring_open, pinky_open]
    
    if all(fingers_open):
        return "JUMP"


    if sum(fingers_open) == 0:
        return "ROLL"

    if index_open and sum([middle_open, ring_open, pinky_open]) == 0:
        index_tip_x = landmarks[8].x
        index_knuckle_x = landmarks[5].x 
        
      
        if index_tip_x < index_knuckle_x - 0.05:
            return "LEFT"
       
        elif index_tip_x > index_knuckle_x + 0.05:
            return "RIGHT"

    return "IDLE"