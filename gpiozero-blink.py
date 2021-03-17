from gpiozero import LED
from time import sleep

led = LED(26)   # Use BCM GPIO (Broadcom) numbering

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)