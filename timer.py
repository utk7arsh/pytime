#! /usr/bin/python

import time
from tkinter import *
from tkinter import messagebox	#message box is used to return the prompt of the end of the timer
# Tk setup
root = Tk()
root.lift()
root.geometry("150x80")
root.attributes('-topmost', True)
root.title("My Timer")

# attributes
hour = StringVar()
minute = StringVar()
second = StringVar()

# default values
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hour_entry= Entry(root, width=3, font=("Time New Roman",16,""),textvariable=hour)
min_entry= Entry(root, width=3, font=("Time New Roman",16,""),textvariable=minute)
sec_entry= Entry(root, width=3, font=("Time New Roman",16,""),textvariable=second)
				
hour_entry.place(x=5,y=10)
min_entry.place(x=55,y=10)
sec_entry.place(x=105,y=10)

def start():
	try:
		start.val = temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
		#print(hour.get)
	except:  #exceptions can be the case where the conversion to an int is not possible eg using alphabets
		print("Please input the right value")
	while temp>-1:
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		min_count,sec_count = divmod(temp,60) 
		hour_count=0

		if min_count >60:		#converting min > 60 to hour and minute accordingly
			hour_count, min_count = divmod(min_count, 60)
		
		hour.set("{0:2d}".format(hour_count))
		minute.set("{0:2d}".format(min_count))
		second.set("{0:2d}".format(sec_count))

		# updating the timer every second using the sleep command of a second
		root.update()
		time.sleep(1)
		# once temp reaches 0 value there will be a message popup as following
		if temp == 0:
			messagebox.showinfo("My Timer", "End of timer!")
		temp -= 1

# def stop():
# 	temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
# 	while temp>-1:
# 		min_count,sec_count = divmod(temp,60) 
# 		hour_count=0

# 		if min_count >60:	
# 			hour_count, min_count = divmod(min_count, 60)
		
# 		hour.set("{0:2d}".format(hour_count))
# 		minute.set("{0:2d}".format(min_count))
# 		second.set("{0:2d}".format(sec_count))
# 		#set and leave it

def restart(): #acts exactly like start() but uses time data from the previous moment of using the start() command
	try:
		#this is used to store the last saved value during the start of the timer
		temp  = start.val
	except:
		print("Please try agin! Something messed up")
	while temp >-1:
		min_count,sec_count = divmod(temp,60) 
		hour_count=0
		if min_count >60:
			hour_count, min_count = divmod(min_count, 60)

		hour.set("{0:2d}".format(hour_count))
		minute.set("{0:2d}".format(min_count))
		second.set("{0:2d}".format(sec_count))

		root.update()
		time.sleep(1)  #1 second sleep

		if (temp <= 0):
			messagebox.showinfo("My Timer", "End of timer!")
		temp -= 1


# buttons display
btn1 = Button(root, text='Start', command= start)
#btn2 = Button(root, text= "Stop", command= stop)
btn3 = Button(root, text = 'Restart', command= restart)

btn1.place(x = 34,y = 50)
#btn2.place(x=50, y=50)
btn3.place(x = 73, y = 50)
root.mainloop()