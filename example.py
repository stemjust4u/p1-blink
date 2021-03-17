from rpigpio import led
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG)

led = led.ledbank(10, mode="BCM")
led.on()
sleep(1)
led.off()