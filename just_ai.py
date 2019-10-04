import serial

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

while True:
	data = int(sensor_ser.readline().decode())
	print("data:", data)
	speed = int(255)
	direction = int(0)
	if data < 10:
		speed = int(0)
	out = [bytes([speed])[0], bytes([direction])[0]]
	motor_ser.write(bytearray(out))
	motor_ser.write(b'\n')
	print("sent command")
	#debug = ser.readline()
	#print("motor:", debug)
