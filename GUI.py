from Tkinter import *
import time
import sys
import os
from detector import Detector as detector
import RPi.GPIO as GPIO



pir_sensor =  11
gas_sensor= 12
metal_sensor= 13
temp_sensor= 15

m10 = 29
m11 = 31
m20 = 33
m21 = 35

GPIO.setmode(GPIO.BOARD)

#GPIO.setup(piezo,GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(gas_sensor, GPIO.IN)
GPIO.setup(metal_sensor, GPIO.IN)
GPIO.setup(temp_sensor, GPIO.IN)

GPIO.setup(m10,GPIO.OUT)
GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m20,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)

GPIO.output(m10,False)
time.sleep(1)
GPIO.output(m11,False)
time.sleep(1)
GPIO.output(m20,False)
time.sleep(1)
GPIO.output(m21,False)
time.sleep(1)

pir_state = 0
gas_state = 0
temp_state = 0
metal_state = 0




#####################functions##########################################

def pir_sen():
	if pir_state == 1: 
		print 'Pir conditon'

def temp_sen():
	if temp_state == 1:
		print 'temperature conditon'

def gas_sen():
	if gas_state == 1:
		print 'gas sensor condition'						
	
def metal_sen():
	if metal_state == 1:
		print 'metal detector condition'
		


















def check_state() :
	print "sensor status"
	pir_state = GPIO.input(pir_sensor)
	print pir_state
	metal_state = GPIO.input(metal_sensor)
	gas_state = GPIO.input(gas_sensor)

	temp_state = GPIO.input(temp_sensor)
def quit():
	print"shuting Down the System..."	
	import sys; sys.exit()
	
def video():
	vid = detector()
	detector.detect()

def forward ():
    print 'moving forward'
    GPIO.output(m10,True)
    
    GPIO.output(m11,False)
    
    GPIO.output(m20,True)
    
    GPIO.output(m21,False)
    
    check_state()
    time.sleep(1)
    pir_sen()
	
def backward():
    print 'moving backward'
    GPIO.output(m10,False)
  
    GPIO.output(m11,True)
    
    GPIO.output(m20,False)
    
    GPIO.output(m21,True)
    
    check_state()
    
def stopp():
    print 'vehicle stop'
    GPIO.output(m10,False)
    
    GPIO.output(m11,False)
    
    GPIO.output(m20,False)
    
    GPIO.output(m21,False)
    
    check_state()
    
def left():
    print 'moving left'
    GPIO.output(m10,False)
    
    GPIO.output(m11,True)
    
    GPIO.output(m20,True)
    
    GPIO.output(m21,False)
    
    check_state()
    
def right():
    print 'moving right'
    GPIO.output(m10,True)
    
    GPIO.output(m11,False)
    
    GPIO.output(m20,False)
    
    GPIO.output(m21,True)
    
    check_state()











######################## Window TITLE ###############################
top1 = Tk()
top1.geometry("420x450+0+0")
top1.title(" survillance vehicle system")
######################## Frame Title #################################

frame = Frame(top1, bd=2, width="600", height="400", relief=SUNKEN)
frame.grid(row=0,column=0)

frame2 = Frame(top1, bd=2, width="200", height="200", relief="raised")
frame2.grid(row=1,column=0)


controlframe = Frame(top1, bd=2, width="200", height="200", relief="raised")
controlframe.grid(row=2,column=0)

frame3 = Frame(top1, bd=2, width="200", height="200",bg="powder blue", relief="raised")
frame3.grid(row=3,column=0)

####################### Frame frame ############################################

label=Label(frame,text="Survillance Vehicle System ", fg='white',bg="black",font=('arial',20,'bold'),bd=5,relief="raised", anchor='center')
label.grid(row=0,column=0)

#================================TIME====================================================
tlocal=time.asctime(time.localtime(time.time()))

#================================INPUT & LABEL FIELD=====================================
label=Label(frame,text=tlocal, fg='white',bg="black",font=('arial',10,'bold'),bd=5,relief="raised", anchor='center')
label.grid(row=1,column=0)

########################### Video Frame ################################

vidbutton = Button(frame2, text="Video", fg="black",padx=100,pady=30, bd=10, command= video, relief= RAISED)
vidbutton.grid(row=0,column=0)



####################### Controll Frame #################################
button1 = Button(controlframe, text="PIR", fg="black",bg='green',bd =10,command = pir_sen, relief= RAISED)
button1.grid(row=0,column=0)

button2 = Button(controlframe,bd=10, text="UP", fg="black",command= forward, relief= RAISED)
button2.grid(row=0,column=1)

button3 = Button(controlframe, text="TEMP", fg="black",bg="green",command= temp_sen, relief= RAISED)
button3.grid(row=0,column=2)

button4 = Button(controlframe,bd=10, text="LEFT", fg="black",command= left , relief= RAISED)
button4.grid(row=1,column=0)

button5 = Button(controlframe,bd=10, text="STOP", fg="black",command= stopp, relief= RAISED)
button5.grid(row=1,column=1)

button6 = Button(controlframe,bd=10, text="RIGHT", fg="black",command= right, relief= RAISED)
button6.grid(row=1,column=2)

button7 = Button(controlframe, text="METEL", fg="black",bg="green",command= metal_sen, relief= RAISED)
button7.grid(row=2,column=0)

button8 = Button(controlframe,bd=10, text="DOWN", fg="black",command= backward, relief= RAISED)
button8.grid(row=2,column=1)

button9 = Button(controlframe, text="GAS", fg="black",bg="green",command= gas_sen, relief= RAISED)
button9.grid(row=2,column=2)


##################### Bottom Frame ################################################



quitbutton = Button(frame3, text="QUIT", fg="black",command=quit, relief= RAISED)
quitbutton.pack(side=RIGHT)







top1.mainloop()


