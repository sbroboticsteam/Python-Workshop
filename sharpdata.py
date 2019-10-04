
import serial

ser = serial.Serial('/dev/ttyACM1',9600)
ser.close()
ser.open()
while True:

    data = ser.readline()
    print(data.decode())

