from digitalio import DigitalInOut
import board
import adafruit_matrixkeypad

def get_keypad(matrix):
    try:
        if matrix == "4x4":
            # Extended 4x4 matrix keypad
            cols = [DigitalInOut(x) for x in (board.D0, board.D1, board.D2, board.D3)]
            rows = [DigitalInOut(x) for x in (board.D4, board.D5, board.D6, board.D7)]
            keys = ((1, 2, 3, "A"), 
                    (4, 5, 6, "B"), 
                    (7, 8, 9, "C"), 
                    ("*", 0, "#", "D"))
        elif matrix == "3x4":
            # Classic 3x4 matrix keypad
            cols = [DigitalInOut(x) for x in (board.D2, board.D0, board.D4)]
            rows = [DigitalInOut(x) for x in (board.D1, board.D6, board.D5, board.D3)]
            keys = ((1, 2, 3),
                    (4, 5, 6),
                    (7, 8, 9),
                    ('*', 0, '#'))
        else:
            raise ValueError(f"Keyboard matrix {matrix} could not be used\n4x4 and 3x4 are the only valid options.")
        return adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
    except Exception as e:
        print(f"Exception: {e}")