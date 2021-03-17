from gpiozero import LED
from time import sleep

led1 = LED(26)   # Use BCM GPIO (Broadcom) numbering
led2 = LED(10)
led1.off()
led2.off()

'''
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
'''
