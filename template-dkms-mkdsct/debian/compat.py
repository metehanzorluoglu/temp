import argparse
import time 
from tflite_support.task import audio
from tflite_support.task import core
from tflite_support.task import processor
from control import get
import numpy as np
import changelog as compass
import serial
import matplotlib.pyplot as plt


def main():
    chunks = []
    line1 = 0
    line2 = 0
    cmp_temp = 0
    line1_temp = 0
    temp = 0
    flag = True
    count_flag = True
    v = [0,1,2,3]
    m = [0] * 4
    t = [0] * 4
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser2 = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
    ser3 = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    with get(16000, 4, 16000 / 1)  as mic:
        compass.test(mic, chunks)
        ser3.write((':').encode('utf-8'))
        for chunk in mic.read_chunks():
            chunks.append(chunk)
            if count_flag == False:
                count_flag = True
                
            if ser.in_waiting > 0:
                line1 = ser.readline().decode('utf-8').rstrip()
                
            if ser2.in_waiting > 0:
                line2 = ser2.readline().decode('utf-8').rstrip()
                
            if max(abs(chunk)) > 30000 and flag == True:
                for i in v:
                    m[i] = chunk[i::4]
                    t[i] = np.argmax(np.abs(m[i]))
                
                print(t)
                cmp = compass.direction_find(t)
                
                ser3.write(('#' + str(int(cmp)) + '/' + str(line1) + '/' + str(line2)  + '\n').encode('utf-8'))
                cmp_temp = cmp
                line1_temp = line1
                flag = False
                count_flag = False

                #plt.plot(chunk)
                #plt.show()
                
            if count_flag == True:
                flag = True
            
            if temp != line2:
                temp = line2
                ser3.write(('#' + str(int(cmp_temp)) + '/' + str(line1_temp) + '/' + str(line2)  + '\n').encode('utf-8'))
            
            chunks = []
            
            
            

if __name__ == '__main__':

    main()