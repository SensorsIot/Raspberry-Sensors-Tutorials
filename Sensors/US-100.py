import time
import board
import busio
import adafruit_us100
import serial

#uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
# Create a US-100 module instance.
us100 = adafruit_us100.US100(uart)

while True:
    print("-----")
    print("Temperature: ", us100.temperature)
    print("Distance: ", us100.distance)
    time.sleep(0.5)