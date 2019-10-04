import serial
import time
from joystick import Joystick

# defines for what serial port motor interface is connected to + baud rate
motor_com_port = '/dev/ttyACM0'
sensor_com_port = '/dev/ttyACM1'
baud = 9600


motor_ser = serial.Serial(motor_com_port, baud)
motor_ser.close()
motor_ser.open()

sensor_ser = serial.Serial(sensor_com_port, baud)
sensor_ser.close()
sensor_ser.open()

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
	speed = 0
	direction = int(0)

	if (joystick.button[0] == True):
		data = int(sensor_ser.readline().decode())
		print("auto mode!")
		print("data", data)

		if data < 10:
			speed = 0
		elif data >= 10:
			speed = 255
	
	elif (joystick.button[1] == False):
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
	motor_ser.write(bytearray(out))
	motor_ser.write(b'\n')
	#debug = ser.readline()
	#print("motors:", debug)
	time.sleep(0.01)
