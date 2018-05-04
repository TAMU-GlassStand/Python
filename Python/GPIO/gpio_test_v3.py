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

gpio.add_event_detect(channel_1, gpio.RISING)
gpio.add_event_detect(channel_2, gpio.RISING)
gpio.add_event_detect(channel_3, gpio.RISING)
gpio.add_event_detect(channel_4, gpio.RISING)
gpio.add_event_detect(channel_5, gpio.RISING)


T=True
F=False

while 1:

	LED1=gpio.event_detected(channel_1)
	LED2=gpio.event_detected(channel_2)
	LED3=gpio.event_detected(channel_3)
	LED4=gpio.event_detected(channel_4)
	LED5=gpio.event_detected(channel_5)

	time.sleep(0.01)
	
	if LED5==T and LED4==F and LED3==F and LED2==F and LED1==F: 
		print"Start"

	if LED5==F and LED4==T and LED3==T and LED2==F and LED1==T: 		
		print"Setting"

	if LED5==F and LED4==T and LED3==T and LED2==T and LED1==F: 		
		print"Google Drive"

	if LED5==F and LED4==T and LED3==T and LED2==T and LED1==T: 				
		print"Removable Storage"
		
	if LED5==F and LED4==T and LED3==T and LED2==F and LED1==F: 		
		print"Brightness Increase"
			
	if LED5==F and LED4==T and LED3==F and LED2==T and LED1==T: 		
		print"Brightness Decrease"

	if LED5==F and LED4==T and LED3==F and LED2==T and LED1==F: 		
		print"Up"

	if LED5==F and LED4==F and LED3==T and LED2==T and LED1==T: 		
		print"Down"

	if LED5==F and LED4==T and LED3==F and LED2==F and LED1==T: 		
		print"Back"

	if LED5==F and LED4==F and LED3==T and LED2==T and LED1==F: 		
		print"Enter"

	if LED5==F and LED4==T and LED3==F and LED2==F and LED1==F: 		
		print"Home Page"

	if LED5==F and LED4==F and LED3==T and LED2==F and LED1==F: 		
		print"Zoom In"
		
	if LED5==F and LED4==F and LED3==T and LED2==F and LED1==T: 		
		print"Zoom Out"
		
	if LED5==F and LED4==F and LED3==F and LED2==T and LED1==F: 		
		print"Previous Page"

	if LED5==F and LED4==F and LED3==F and LED2==F and LED1==T: 		
		print"Next Page"

	if LED5==F and LED4==F and LED3==F and LED2==T and LED1==T: 		
		print"Fit to Page"



