import pyautogui
from PIL import Image
import pytesseract
import cv2


def get_mouse_coordinates():
    print("Move your mouse to the desired location...")
    pyautogui.PAUSE = 2000  # Add a pause to allow time for positioning
    pyautogui.sleep(4)
    x, y = pyautogui.position()
    print("Coordinates:", x, y)

def main2(name):
    # Capture a screenshot
    # Define the coordinates of the minimize button
    pyautogui.sleep(.5)
    minimize_button_x = 1269
    minimize_button_y = 340

    # Move the mouse to the minimize button
    pyautogui.moveTo(minimize_button_x, minimize_button_y, duration=.2)
    pyautogui.sleep(.5)
    pyautogui.click()
    # Pause for a brief moment to ensure the minimize animation is complete
    pyautogui.sleep(.5)

    # Capture a screenshot
    screenshot = pyautogui.screenshot()
    name1 = name + ".png"
    screenshot.save(name1)
    main3(name)
    main4(name)
    #closes the app
    minimize_button_x2 = 1600
    minimize_button_y2 = 79

    # Move the mouse to the minimize button
    pyautogui.moveTo(minimize_button_x2, minimize_button_y2, duration=.2)
    pyautogui.sleep(.5)
    pyautogui.click()
    pyautogui.moveTo(minimize_button_x2 - 40, minimize_button_y2 - 9, duration=.2)
    pyautogui.click()
    pyautogui.moveTo(minimize_button_x, minimize_button_y, duration=.2)
    print("Screenshot taken after minimizing the screen.")


def main3(name):
    pyautogui.sleep(.5)
    minimize_button_x = 1296
    minimize_button_y = 420

    # Move the mouse to the minimize button
    pyautogui.moveTo(minimize_button_x, minimize_button_y, duration=.2)
    pyautogui.sleep(.5)
    pyautogui.click()
    # Pause for a brief moment to ensure the minimize animation is complete
    pyautogui.sleep(.5)

    # Capture a screenshot
    screenshot = pyautogui.screenshot()
    name = name + "-1.png"
    screenshot.save(name)

def main4(name):
    pyautogui.sleep(.5)
    minimize_button_x = 486
    minimize_button_y = 766

    # Move the mouse to the minimize button
    pyautogui.moveTo(minimize_button_x, minimize_button_y, duration=.2)
    pyautogui.sleep(.5)
    pyautogui.click()
    # Pause for a brief moment to ensure the minimize animation is complete
    pyautogui.sleep(.5)

    # Capture a screenshot
    screenshot = pyautogui.screenshot()
    name = name + "-2.png"
    screenshot.save(name)


def scrolling(x):
    minimize_button_x = 1269
    minimize_button_y = 340
    pyautogui.mouseDown(minimize_button_x, minimize_button_y)
    pyautogui.move(0, -100 * x, duration=1)
    pyautogui.mouseUp()

    return x
def main():
    case = 0;
    for x in range(295):
        name = "ScreenShot" + str(x);
        main2(name);
        if case == 0:
            z = (x % 3) + 1
            scrolling(z)
            if(z == 3):
                case = 1
        else:
            scrolling(3)
if __name__ == "__main__":
    main()
