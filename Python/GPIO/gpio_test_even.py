#!/usr/bin/python

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import RPi.GPIO as gpio
import time

m=PyMouse()
k=PyKeyboard()

x_dim, y_dim=m.screen_size()
x_pos=x_dim/100
y_pos=y_dim/100

x_pdf=x_pos*23
y_pdf=y_pos*22


prev=-1
file_sel=-1
user_location=-1 # Used to determine where the user is: 0=Settings, 1=Google Drive, 2=Removeable Storage
pdf_view=-1 	 # Used to determine how the pdf is being displayed: 0=???, 1=Google Drive Preview, 2=Chrome Viewer
enter_count=0
zoom_count=0
zoom_page=0 # Temporary variable to switch buttons from zoom to next page 
zoom_usb=-1

trigger=0
prev=-1

#GPIO STUFF

#Captivate MSP430 Pins
#LED1 = P1.7
#LED2 = P1.6
#LED3 = P1.0
#LED4 = P2.2
#LED5 = P1.1


gpio.setmode(gpio.BOARD)

channel_1=35
channel_2=36
channel_3=37
channel_4=38
channel_5=40

gpio.setup(channel_1, gpio.IN, pull_up_down = gpio.PUD_DOWN) #LED1
gpio.setup(channel_2, gpio.IN, pull_up_down = gpio.PUD_DOWN) #LED2
gpio.setup(channel_3, gpio.IN, pull_up_down = gpio.PUD_DOWN) #LED3
gpio.setup(channel_4, gpio.IN, pull_up_down = gpio.PUD_DOWN) #LED4
gpio.setup(channel_5, gpio.IN, pull_up_down = gpio.PUD_DOWN) #LED5



def read_gpio():

	LED1=gpio.input(channel_1)
	LED2=gpio.input(channel_2)
	LED3=gpio.input(channel_3)
	LED4=gpio.input(channel_4)
	LED5=gpio.input(channel_5)

	LED_code = [LED5, LED4, LED3, LED2, LED1]

	print"Testin"
	
	if LED_code==[1, 0, 0, 0, 0]:
		trigger=1
		print"Start"
		
	elif LED_code==[0, 1, 1, 0, 1]:
		print"Setting"

	elif LED_code==[0, 1, 1, 1, 0]:
		print"Google Drive"
		trigger=1
		
	elif LED_code==[0, 1, 1, 1, 1]:
		print"Removable Storage"
		trigger=1
		
	elif LED_code==[0, 1, 1, 0, 0]:
		print"Brightness Increase"
		trigger=1
			
	elif LED_code==[0, 1, 0, 1, 1]:
		print"Brightness Decrease"
		trigger=1

	elif LED_code==[0, 1, 0, 1, 0]:
		print"Up"

	elif LED_code==[0, 0, 1, 1, 1]:
		print"Down"

	elif LED_code==[0, 1, 0, 0, 1]:
		print"Back"

	elif LED_code==[0, 0, 1, 1, 0]:
		print"Enter"

	elif LED_code==[0, 1, 0, 0, 0]:
		print"Home Page"

	elif LED_code==[0, 0, 1, 0, 0]:
		print"Zoom In"
		
	elif LED_code==[0, 0, 1, 0, 1]:
		print"Zoom Out"
		
	elif LED_code==[0, 0, 0, 1, 0]:
		print"Previous Page"

	elif LED_code==[0, 0, 0, 0, 1]:
		print"Next Page"

	elif LED_code==[0, 0, 0, 1, 1]:
		print"Fit to Page"
	else: 
		trigger=0

	return;



#gpio.add_event_detect(channel_1, gpio.RISING, callback = read_gpio, bouncetime=100)

#gpio.add_event_detect(channel_2, gpio.RISING, callback = read_gpio, bouncetime=100)
#gpio.add_event_detect(channel_3, gpio.RISING, callback = read_gpio, bouncetime=100)
#gpio.add_event_detect(channel_4, gpio.RISING, callback = read_gpio, bouncetime=100)
gpio.add_event_detect(channel_5, gpio.RISING, callback = read_gpio, bouncetime=100)

while 1:
	print"no input"

