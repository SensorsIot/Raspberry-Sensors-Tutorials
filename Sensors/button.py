import time
import board
import digitalio

print("press the button!")

led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    buttonState = button.value
    led.value = not buttonState # light when button is pressed!
