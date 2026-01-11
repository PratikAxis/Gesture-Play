import pyautogui

class GameController:
    def __init__(self):
        # PyAutoGUI safety: move mouse to corner to abort if things go wrong
        pyautogui.FAILSAFE = True 
        
    def perform_action(self, gesture):
        if gesture == "JUMP":
            pyautogui.press('up')    # Or 'w' depending on your settings
            print("ACTION: JUMP")
            
        elif gesture == "ROLL":
            pyautogui.press('down')  # Or 's'
            print("ACTION: ROLL")
            
        elif gesture == "LEFT":
            pyautogui.press('left')  # Or 'a'
            print("ACTION: LEFT")
            
        elif gesture == "RIGHT":
            pyautogui.press('right') # Or 'd'
            print("ACTION: RIGHT")
            
        else:
            pass # IDLE - do nothing