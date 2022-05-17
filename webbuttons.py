#!/usr/bin/python3
import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

import RPi.GPIO as GPIO
import datetime
import subprocess
import signal
import time


class GracefulKiller:
    """Handles the service daemon control"""
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


class WebButtonControl:
    """Main Code for GPIO Control and Key firing"""
    isActive = False

    def __init__(self):
        # Setup GPIO
        GPIO.setwarnings(True) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(32, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
        GPIO.add_event_detect(36, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
        GPIO.add_event_detect(38, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
        GPIO.add_event_detect(40, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)

        isActive = True

    def button_callback(self, channel):
        subprocess.call(["xdotool", "search", "--onlyvisible", "--class", "Chromium", "windowactivate"])
        if (channel == 32):
            # 1 = W
            subprocess.call(["xdotool", "keydown", "w"])
            subprocess.call(["xdotool", "keyup", "w"])
        elif (channel == 36):
            # 2 = C
            subprocess.call(["xdotool", "keydown", "c"])
            subprocess.call(["xdotool", "keyup", "c"])
        elif (channel == 38):
            # 3 = M
            subprocess.call(["xdotool", "keydown", "m"])
            subprocess.call(["xdotool", "keyup", "m"])
        elif (channel == 40):
            # 4 = P
            subprocess.call(["xdotool", "keydown", "p"])
            subprocess.call(["xdotool", "keyup", "p"])
            
    def exitnow(self):
        GPIO.cleanup() # Clean up
        isActive = False



# ###########################
# Sub Main()
if __name__ == '__main__':
    killer = GracefulKiller()
    webbut = WebButtonControl()
    while not killer.kill_now:
        time.sleep(1)
    
    webbut.exitnow()
