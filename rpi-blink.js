// Install onoff with 
// $ npm install onoff 

var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(26, 'out'); //use GPIO BCM number (Broadcom), and specify that it is output
var blinkInterval = setInterval(blinkLED, 250); //run the blinkLED function every 250ms

function blinkLED() {             
  if (LED.readSync() === 0) {     //check the pin state, if the state is 0 (or off)
    LED.writeSync(1);             //set pin state to 1 (turn LED on)
  } else {
    LED.writeSync(0);             //set pin state to 0 (turn LED off)
  }
}

function endBlink() { 
  clearInterval(blinkInterval);   // Stop blink intervals
  LED.writeSync(0);               // Turn LED off
  LED.unexport();                 // Free resources
}


setTimeout(endBlink, 5000); //stop blinking after 5 seconds

/* Other timing functions in javascript
setTimeout(function, milliseconds)
Executes a function, after waiting a specified number of milliseconds.

setInterval(function, milliseconds)
Same as setTimeout(), but repeats the execution of the function continuously. */