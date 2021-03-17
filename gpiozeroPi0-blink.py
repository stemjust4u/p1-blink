'''
Control internal Pi0 LED
First disable the usual triggers for the built-in LEDs.

$ echo none | sudo tee /sys/class/leds/led0/trigger
$ echo gpio | sudo tee /sys/class/leds/led1/trigger

To revert the LEDs to their usual purpose you can either reboot your Pi or run the following commands:

$ echo mmc0 | sudo tee /sys/class/leds/led0/trigger
$ echo input | sudo tee /sys/class/leds/led1/trigger
'''

from gpiozero import LED
from signal import pause

activity = LED(47, active_high=False) # /sys/class/leds/led0

activity.blink()
pause()
