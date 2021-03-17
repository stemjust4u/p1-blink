import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)  # BCM=GPIO (Broadcom), BOARD=1-40 board numbering
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(26, GPIO.HIGH) 
 sleep(1) 
 GPIO.output(26, GPIO.LOW) 
 sleep(1) 