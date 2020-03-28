
"""
@author: Engr.Muhammad Taha

"""

import os
import tkinter
from PIL import Image
import serial
import time
import RPi.GPIO as GPIO
import socket

#Data Variable Initalize
SensorsData = "0,0,0,0,0,0,0,0,0"
x = (SensorsData.split(',', 8)) 



#Initialize Serial Port
ser = serial.Serial('/dev/ttyUSB0', 115200)

#Initialize Time
localtime=time.asctime(time.localtime(time.time()))

#Find IP Address
def get_ip_address():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

#Graphical User Interface 
top = tkinter.Tk()
top.geometry("1920x1080")
#top.attributes('-fullscreen', True)
top.title("Distribution Panel Monitoring (Indus University)")

image = tkinter.PhotoImage(file="Indus_Logo.png")
LOGO = tkinter.Label( image=image )
LOGO.pack()
LOGO.place(x= 10, y= 1)

Name =tkinter.Label(top, text="3-PHASE DISTRIBUTION PANEL MONITORING",font=('arial', 22), bd = 4, fg="Dark Blue" )
Name.pack()
Name.place(x=270 , y= 45)

Time =tkinter.Label(top, text=localtime,font=('arial', 10), bd = 2, fg="black")
Time.pack()
Time.place(x= 810, y= 8)


IP =tkinter.Label(top, text=get_ip_address(),font=('arial', 10), bd = 2, fg="black")
IP.pack()
IP.place(x= 850, y= 28)


################################### PHASE 1 ###########################################

P1 =tkinter.Label(top, text="PHASE-1 MONITORING",font=('arial', 14), bd = 5, fg="Black")
P1.pack()
P1.place(x= 100, y= 200)

L1 =tkinter.Label(top, text="Voltage (V) :",font=('arial', 14), bd = 5, fg="Dark Blue")
L1.pack()
L1.place(x= 130, y= 250)

L1R =tkinter.Label(top, text=x[1]+" V",font=('arial', 14), bd = 5, fg="red")
L1R.pack()
L1R.place(x= 240, y= 250)

C1 =tkinter.Label(top, text="Current (A) :",font=('arial', 14), bd = 5, fg="Dark Blue")
C1.pack()
C1.place(x= 130, y= 300)

C1R =tkinter.Label(top, text=x[2]+" A",font=('arial', 14), bd = 5, fg="red")
C1R.pack()
C1R.place(x= 240, y= 300)

################################### PHASE 2 ###########################################

P2 =tkinter.Label(top, text="PHASE-2 MONITORING",font=('arial', 14), bd = 5, fg="Black")
P2.pack()
P2.place(x= 400, y= 200)

L2 =tkinter.Label(top, text="Voltage (V) :",font=('arial', 14), bd = 5, fg="Dark Blue")
L2.pack()
L2.place(x= 430, y= 250)

L2R =tkinter.Label(top, text=x[3]+" V",font=('arial', 14), bd = 5, fg="red")
L2R.pack()
L2R.place(x= 540, y= 250)

C2 =tkinter.Label(top, text="Current (A) :",font=('arial', 14), bd = 5, fg="Dark Blue")
C2.pack()
C2.place(x= 430, y= 300)

C2R =tkinter.Label(top, text=x[4]+" A",font=('arial', 14), bd = 5, fg="red")
C2R.pack()
C2R.place(x= 540, y= 300)



################################### PHASE 3 ###########################################

P3 =tkinter.Label(top, text="PHASE-3 MONITORING",font=('arial', 14), bd = 5, fg="Black")
P3.pack()
P3.place(x= 700, y= 200)

L3 =tkinter.Label(top, text="Voltage (V) :",font=('arial', 14), bd = 5, fg="Dark Blue")
L3.pack()
L3.place(x= 730, y= 250)

L3R =tkinter.Label(top, text=x[3]+" V",font=('arial', 14), bd = 5, fg="red")
L3R.pack()
L3R.place(x= 840, y= 250)

C3 =tkinter.Label(top, text="Current (A) :",font=('arial', 14), bd = 5, fg="Dark Blue")
C3.pack()
C3.place(x= 730, y= 300)

C3R =tkinter.Label(top, text=x[4]+" A",font=('arial', 14), bd = 5, fg="red")
C3R.pack()
C3R.place(x= 840, y= 300)


#--------------------Power Factor & Motor------------#
PowerFactor =tkinter.Label(top, text="Power Factor (0 - 1):",font=('arial', 14), bd = 2, fg="Black")
PowerFactor.pack()
PowerFactor.place(x= 100, y= 400)

PFValue =tkinter.Label(top, text=x[7],font=('arial', 14), bd = 2, fg="red")
PFValue.pack()
PFValue.place(x= 280, y= 400)

#PFC =tkinter.Label(top, text="PFC Unit Status :",font=('arial', 14), bd = 2, fg="Black")
#PFC.pack()
#PFC.place(x= 400, y= 400)

#PFCStatus =tkinter.Label(top, text="On",font=('arial', 14), bd = 2, fg="RED")
#PFCStatus.pack()
#PFCStatus.place(x= 550, y= 400)

Motor =tkinter.Label(top, text="Motor Status :",font=('arial', 16), bd = 2, fg="Black")
Motor.pack()
Motor.place(x= 700, y= 400)

MotorStatus =tkinter.Label(top, text="N/A",font=('arial', 16), bd = 2, fg="red")
MotorStatus.pack()
MotorStatus.place(x= 835, y= 400)

def ReadSerial() :
    global x
    #threading.Timer(1.0, ReadSerial).start()
    if(ser.in_waiting >0):
        line = str (ser.readline())
        x = line.split(',', 8 )
        print(x)
        L1R.configure(text=str(x[1]))
        L2R.configure(text=str(x[3]))
        L3R.configure(text=str(x[5]))
        C1R.configure(text=str(round((float (x[2]) )
        C2R.configure(text=str(round((float (x[4]) )
        C3R.configure(text=str(round((float (x[6]) )
        PFValue.configure(text=str(x[7]))
        
        
        global localtime
        localtime=time.asctime(time.localtime(time.time()))
        Time.configure(text=localtime)

def read_every_second():
    
    ReadSerial()
    top.after(100, read_every_second)

read_every_second()
top.mainloop()

