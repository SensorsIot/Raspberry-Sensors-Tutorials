import time
import board
import digitalio

print("I am waiting for movements")

led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT

pirSensor = digitalio.DigitalInOut(board.D13)
pirSensor.direction = digitalio.Direction.INPUT
pirSensor.pull = digitalio.Pull.UP

while True:
    led.value = pirSensor.value # light LED when PIR is on!
    if pirSensor.value==True:
       print ("Intrusion detected")
       time.sleep(2)
    else:
       print ("Calm")
       time.sleep(2)
