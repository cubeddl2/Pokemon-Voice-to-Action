import vgamepad as vg
import speech_recognition as sr
import time

gamepad = vg.VDS4Gamepad()
recognizer = sr.Recognizer()

def press_square():
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    time.sleep(0.4)
    gamepad.update()
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    print("Pressed SQUARE")

def press_triangle():
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    time.sleep(0.4)
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    print("Pressed TRIANGLE")

def press_circle():
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    time.sleep(0.4)
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    print("Pressed CIRCLE")

def press_cross():
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    time.sleep(0.4)
    gamepad.update()
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    print("Pressed CROSS")

def press_rs():
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    time.sleep(0.4)
    gamepad.update()
    gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    gamepad.release_button(button = vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
    gamepad.update()
    print("Pressed RS")

run = True
while run == True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio).lower()

            match text:
                case 'shuriken':
                    press_triangle()
                    print("Greninja used Water Shuriken")
                case 'ice beam':
                    press_circle()
                    print("Greninja used Ice Beam")
                case 'hydro pump':
                    press_square()
                    print("Greninja used Hydro Pump")
                case 'mega shinka':
                    press_rs()
                    print("Mega Shinka!")
                case 'mega evolve':
                    press_rs()
                    print("Mega Evolution!")
                case 'exit':
                    run == False

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
    except (OSError, IOError):
        recognizer = sr.Recognizer()
        time.sleep(1.5)
        continue