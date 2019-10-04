import serial
import time
from joystick import Joystick

# defines for what serial port motor interface is connected to + baud rate
com_port = '/dev/ttyACM0'
baud = 9600


ser = serial.Serial(com_port, baud)
ser.close()
ser.open()

joystick = Joystick()

prev_dir = -1
prev_speed = -1

while True:
	#speed = int(input("speed:"))
	#print("speed:", speed)
	#dir_input = int(input("direction:"))
	#direction = 0
	#if dir_input == 1:
	#	direction = 1
	#elif dir_input == 0:
	#	direction = 0
	#print("dir:",direction)
	
	joystick.update()
	
	speed = int(joystick.axis[1])
	if speed == prev_speed:
		continue
	else:
		prev_speed = speed

	direction = 0
	if speed >= 0:
		direction = 0
	elif speed < 0:
		direction = 1
	
	direction = int(direction)
	print("speed:", speed, "direction:",direction)
	out = [bytes([int(abs(speed))])[0], bytes([direction])[0]]
	ser.write(bytearray(out))
	ser.write(b'\n')
	#debug = ser.readline()
	#print("motors:", debug)
	time.sleep(0.01)
