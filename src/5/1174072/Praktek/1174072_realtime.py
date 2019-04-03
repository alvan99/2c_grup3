# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:03:12 2019

@author: Frnn
"""

import serial


import serial

def ambilData():
    ser = serial.Serial('COM5',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ambilData()

import serial
import csv

def writeCsv():
    ser = serial.Serial('COM5',9600)
    with open('1174087.csv', mode='w') as csv_file:
        fieldnames = ['jarak']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        while (1):
            data_praktek = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'jarak': data_praktek})