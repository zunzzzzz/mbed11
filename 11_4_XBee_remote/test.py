import serial

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

# send to remote
print("send message")
s.write("abcd\r\n".encode())
line = s.read(5)
print('Get:', line.decode())

s.close()