import RPi.GPIO as GPIO 
from time import sleep
import logging

class ledbank:
    def __init__(self, pins, delay= 1, warnings=False, mode='BCM'):
        self.pins = pins
        self.delay = delay
        GPIO.setwarnings(warnings)
        if mode == 'BCM':
            GPIO.setmode(GPIO.BCM)  # BCM=GPIO (Broadcom)
        elif mode == 'BOARD':
            GPIO.setmode(GPIO.BOARD)  #BOARD=1-40 board numbering
        else:
            logging.info("invalid mode")
            exit()
        GPIO.setup(self.pins, GPIO.OUT, initial=GPIO.LOW)

    def on(self):
        GPIO.output(self.pins, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pins, GPIO.LOW)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    led = ledbank(10, mode="BCM")
    led.on()
    sleep(1)
    led.off()
