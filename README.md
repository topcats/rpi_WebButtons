# rpi_WebButtons
Using Raspberry PI GPIO input buttons to control a kiosk web browser

## Hardware
* 1x4 Matrix Extension Keyboard 4 Key Membrane Switch Keypad Keyboard
* Assorted Dupont Wire Cable Jumper Pins Header Connector Kit & M/F Crimp
* 8AWG to 30AWG Flexible Silicone Wire Cable (Colour:Black, Length:10 Metres, Size:26AWG)

### Tools
* Pin Crimp Plier Tool 2.54mm 3.96mm 18-28 AWG Crimper For Dupont

> Use a multi-meter to determine the pin out configuration, as they can all be different.

> Find the common neutral first


## Python Button Press Event Listening
### General Setup
```python
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
```

### Pin Setup
Use ```GPIO.PUD_UP``` to use internal resistors.

Use Pin Numbers not GPIO numbers.

```python
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
```

### Callback Function
```python
def button_callback(channel):
    print("Button was pushed!")
    print(channel) #pin number
```
```python
# Setup for pin 32 when the voltage drops, do callback, but prevent double press for 1 second.
GPIO.add_event_detect(32, GPIO.FALLING, callback=button_callback, bouncetime=1000)
```

### Clean down at exit
```python
GPIO.cleanup() # Clean up
```


## Transmit Keys to Chromium Web Browser
```python
import subprocess
```
Send ```w``` key to browser, after activating the window
```python
subprocess.call(["xdotool", "search", "--onlyvisible", "--class", "Chromium", "windowactivate"])
subprocess.call(["xdotool", "keydown", "w"])
subprocess.call(["xdotool", "keyup", "w"])
```


## Web Page Changes
There will be a little bit of work required on the webpage itself to accept the input keys.

### JQuery Method
Using jQuery at the bottom of the page:

```javascript
$(document).ready(function() {

    // Set Keyboard listener
    window.onkeydown= function(gfg){
        if(gfg.keyCode === 32){
            // R = Reload
            location.reload(false);

        } else if (gfg.keyCode == 87) {
            // W = Do Work 
            doWebpageWork();
        } else {
            console.log(gfg.keyCode);
        };
    };
});
```
