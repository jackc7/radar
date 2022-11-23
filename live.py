import serial
import timeit

def main():
    global ser
    with open("output.txt", 'wb') as f:
        print("start")
        f.write(ser.read(100000))
        print("end")

ser = serial.Serial('COM3', 115200)  # open serial port
t = timeit.timeit(main, number=1)
ser.close()             # close port
print(str(t))