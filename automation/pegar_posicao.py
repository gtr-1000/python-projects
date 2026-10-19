import os
import sys
import time
import pyautogui

print("=== MOUSE POSITION TRACKER ===")
print("Move your mouse around the screen to see the X and Y coordinates.")
print("Press CTRL + C in the terminal to stop the program.\n")

try:
    while True:
        # Get current mouse coordinates
        x, y = pyautogui.position()

        # Format the position text with padding so it stays aligned
        position_str = f"X: {str(x).rjust(4)} | Y: {str(y).rjust(4)}"

        # Print the coordinates to the console
        sys.stdout.write(position_str)
        sys.stdout.flush()

        # Wait a short moment before updating
        time.sleep(0.5)

        # Erase the current line to overwrite it in the next loop
        sys.stdout.write("\r")

except KeyboardInterrupt:
    print("\n\nProgram stopped by user.")
