# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:12:51 2019

@author: ASUS
"""

import serial 
def tryExcepError():
    try:
        ser = serial.serial('COM4',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except TypeError:
        print ("Terjadi ketidaksamaan type")
        

tryExcepError()