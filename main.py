import serial
import timeit

def main():
    global ser
    with open("output.txt", 'wb') as f:
        f.write(ser.read(100000))

ser = serial.Serial('COM3', 115200)  # open serial port
t = timeit.timeit(main, number=1)
ser.close()             # close port
print(t)