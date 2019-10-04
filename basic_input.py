import serial

# defines for what serial port motor interface is connected to + baud rate
com_port = '/dev/ttyACM0'
baud = 9600


ser = serial.Serial(com_port, baud)
ser.close()
ser.open()

while True:
	speed = int(input("speed:"))
	print("speed:", speed)
	dir_input = int(input("direction:"))
	direction = 0
	if dir_input == 1:
		direction = 1
	elif dir_input == 0:
		direction = 0
	print("dir:",direction)
	out = [bytes([speed])[0], bytes([direction])[0]]
	ser.write(bytearray(out))
	ser.write(b'\n')
	#debug = ser.readline()
	#print("motor:", debug)
