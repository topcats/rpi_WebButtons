# rpi_WebButtons
Using Raspberry PI GPIO input buttons to control a kiosk web browser

## Hardware

## Python Button Press Event Listening


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
            // W = Weather 
            currentPane = "photo";
            nextPaneManual();

        } else if (gfg.keyCode == 67) {
            // C = Calendar
            currentPane = "weather";
            nextPaneManual();

        } else if (gfg.keyCode == 77) {
            // M = Menu
            currentPane = "calendar";
            nextPaneManual();

        } else if (gfg.keyCode == 80) {
            // P = Photos
            currentPane = "menu";
            nextPaneManual();

        } else {
            console.log(gfg.keyCode);
        };
    };
});
```