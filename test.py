import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import datetime

def button_callback(channel):
    print(datetime.datetime.now())
    print("Button was pushed!")
    print(channel)

GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(32, GPIO.BOTH, callback=button_callback, bouncetime=1000)
GPIO.add_event_detect(36, GPIO.BOTH, callback=button_callback, bouncetime=1000)
GPIO.add_event_detect(38, GPIO.BOTH, callback=button_callback, bouncetime=1000)
GPIO.add_event_detect(40, GPIO.BOTH, callback=button_callback, bouncetime=1000)


print(datetime.datetime.now())
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up



