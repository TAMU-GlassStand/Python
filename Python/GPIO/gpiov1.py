#!/usr/bin/python

from smbus2 import SMBus
from smbus2 import SMBusWrapper
from pymouse import PyMouse
from pykeyboard import PyKeyboard
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


channel_1=
channel_2=
channel_3=
channel_4=
channel_5=

GPIO.setup(channel_1, GPIO.IN) #LED1
GPIO.setup(channel_2, GPIO.IN) #LED2
GPIO.setup(channel_3, GPIO.IN) #LED3
GPIO.setup(channel_4, GPIO.IN) #LED4
GPIO.setup(channel_5, GPIO.IN) #LED5



while 1:

	LED1=GPIO.input(channel_1)
	LED2=GPIO.input(channel_1)
	LED3=GPIO.input(channel_1)
	LED4=GPIO.input(channel_1)
	LED5=GPIO.input(channel_1)

	LED_code = [LED5, LED4, LED3, LED2, LED1]
	print "LED values : %s" % LED_code
	time.sleep(1)

	
	
	if read3==0:
		print"Button 1 was pressed: Start"

		# Start/Restart
		k.press_key(k.control_key)
		k.tap_key('w')
		time.sleep(0.5)
		k.tap_key('w')
		k.release_key(k.control_key)

		time.sleep(1)

		k.press_key(k.shift_key)
		k.press_key(k.alt_key)
		k.tap_key('t')
		k.release_key(k.shift_key)
		k.release_key(k.alt_key)

	elif read3==5:
		print"Button 6 was pressed: Setting"
		
		#Settings
		m.move(x_pos*9, y_pos*15)
		m.click(x_pos*9, y_pos*15, 1)
		user_location=0	#Flag so buttons 2 and 3 only click if on the settings page		


	elif read3==9:
		print"Button 10 was pressed: Google Drive"
		
		#Google Drive
		m.move(x_pos*9, y_pos*45)
		m.click(x_pos*9, y_pos*45, 1)
		user_location=1
		time.sleep(1)
		k.tap_key(k.tab_key, 3)
	


	elif read3==13:
		print"Button 14 was pressed: Removable Storage"
		
		# Removable Storage

		m.move(x_pos*9, y_pos*80)
		m.click(x_pos*9, y_pos*80)
		user_location=2
		time.sleep(1)
		k.tap_key(k.tab_key)

	elif read3==2:
		print"Button 3 was pressed: Brightness Increase"

		# Brightness Increase
		if user_location==0:
			# Brightness Plus
			m.move(x_pos*30, y_pos*21.25)
			m.click(x_pos*30, y_pos*21.25, 1)

			# Apply Changes  
			m.move(x_pos*26, y_pos*22.5)
			m.click(x_pos*26, y_pos*22.5, 1)
			

			
	elif read3==12:
		print"Button 13 was pressed: Brightness Decrease"

		# Brightness Decrease
		if user_location==0:
			# Brightness Minus
			m.move(x_pos*35.25, y_pos*21.25)
			m.click(x_pos*35.25, y_pos*21.25, 1)

			# Apply Changes
			m.move(x_pos*26, y_pos*22.5)
			m.click(x_pos*26, y_pos*22.5, 1)



			
	elif read3==8:
		print"Button 9 was pressed: Up"

		# Up
		if user_location==1 and enter_count==0:
			k.press_key(k.shift_key)
			k.tap_key(k.tab_key, 2)
			k.release_key(k.shift_key)
		
		elif user_location==2:
			k.press_key(k.shift_key)
			k.tap_key(k.tab_key)
			k.release_key(k.shift_key)




	elif read3==11:
		print"Button 12 was pressed: Down"

		#Down
		if user_location==1 and enter_count==0:
			k.tap_key(k.tab_key, 2)

		elif user_location==2:
			k.tap_key(k.tab_key)



	elif read3==4:
		print"Button 5 was pressed: Back"

		#Back

		if user_location==1 and enter_count==1:
			k.press_key(k.control_key)
			k.tap_key('w')
			k.release_key(k.control_key)
			enter_count=0
			
		if user_location==2:
			k.press_key(k.alt_key)
			k.tap_key(k.left_key)
			k.release_key(k.alt_key)
			enter_count=0



	if read3==7:
		print"Button 8 was pressed: Enter"

		# Enter

		if user_location==1:
			k.tap_key(k.enter_key)
			enter_count=1
		
		if user_location==2:
			k.tap_key(k.enter_key)
			time.sleep(0.1)
			k.tap_key(k.tab_key)
			enter_count=1
		

	if read3==1:
		print"Button 2 was pressed: Home Page"

		# Home Page
		if zoom_page==0:
			zoom_page=1
		else:
			zoom_page=0

	if read3==14:
		print"Button 15 was pressed: Zoom In"

		# Zoom In
		# NOT WORKING ON EIC BOARD

		if user_location==1: 
			k.press_key(k.control_key)
			k.tap_key('=')
			k.release_key(k.control_key)
			zoom_count=zoom_count+1

		if user_location==2:
			k.press_key(k.control_key)
			k.tap_key('=')
			k.release_key(k.control_key)
			zoom_count=zoom_count+1

	if read3==15:
		print"Button 16 was pressed: Zoom Out"

		# Zoom Out
		# NOT WORKING ON EIC BOARD

		if user_location==1: 
			k.press_key(k.control_key)
			k.tap_key('-')
			k.release_key(k.control_key)
			zoom_count=zoom_count-1

		if user_location==2:
			k.press_key(k.control_key)
			k.tap_key('-')
			k.release_key(k.control_key)
			zoom_count=zoom_count-1

	if read3==6:
		print"Button 7 was pressed: Previous Page"

		# Previous Page
		if user_location==1 and enter_count==1 and zoom_page==0:
			k.tap_key('k')
		
		if user_location==2 and zoom_page==0:
			k.tap_key(k.left_key)
		
		if user_location==1 and zoom_page==1:
			k.press_key(k.control_key)
			k.tap_key('-')
			k.release_key(k.control_key)
			zoom_count=zoom_count-1		

		if user_location==2 and zoom_page==1:
			if zoom_usb==-1:
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.enter_key)
				zoom_usb=2

			if zoom_usb==0: #On the fit to page button
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.enter_key)
				zoom_usb=2

			if zoom_usb==1: #On the + button
				k.tap_key(k.tab_key)
				k.tap_key(k.enter_key)
				zoom_usb=2

			if zoom_usb==2: #On the - button
				k.tap_key(k.enter_key)	
				zoom_usb=2

	if read3==3:
		print"Button 4 was pressed: Next Page"

		# Next Page
		if user_location==1 and enter_count==1 and zoom_page==0:
			k.tap_key('j')
		
		if user_location==2 and zoom_page==0:
			k.tap_key(k.right_key)

		if user_location==1 and zoom_page==1:
			k.press_key(k.control_key)
			k.tap_key('=')
			k.release_key(k.control_key)
			zoom_count=zoom_count+1

		if user_location==2 and zoom_page==1:
			if zoom_usb==-1:
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key)
				time.sleep(0.1)
				k.tap_key(k.enter_key)
				zoom_usb=1

			if zoom_usb==0: #On the fit to page button
				k.tap_key(k.tab_key)
				k.tap_key(k.enter_key)
				zoom_usb=1

			if zoom_usb==1: #On the + button
				k.tap_key(k.enter_key)
				zoom_usb=1

			if zoom_usb==2: #On the - button
				k.press_key(k.shift_key)
				k.tap_key(k.tab_key)
				k.release_key(k.shift_key)
				k.tap_key(k.enter_key)
				zoom_usb=1

	if read3==10:
		print"Button 11 was pressed: Fit to Page"

		# Fit to Page
		# Zoom is currently not working
		if user_location==1:
			if zoom_count>0:
				while zoom_count>0:
					k.press_key(k.control_key)
					k.tap_key('-')
					k.release_key(k.control_key)
					zoom_count=zoom_count-1				

			if zoom_count<0:
				while zoom_count<0:
					k.press_key(k.control_key)
					k.tap_key('=')
					k.release_key(k.control_key)
					zoom_count=zoom_count+1	

		if user_location==2:
			if zoom_usb==-1:
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.tap_key(k.tab_key, 1)
				k.tap_key(k.enter_key)
				zoom_usb=0

			elif zoom_usb==0: #On the fit to page button
				k.tap_key(k.enter_key)
				zoom_usb=0

			elif zoom_usb==1: #On the + button
				k.press_key(k.shift_key)
				k.tap_key(k.tab_key)
				k.release_key(k.shift_key)
				k.tap_key(k.enter_key)
				zoom_usb=0

			elif zoom_usb==2: #On the - button
				k.press_key(k.shift_key)
				k.tap_key(k.tab_key, 2)
				time.sleep(0.1)
				k.release_key(k.shift_key)
				k.tap_key(k.enter_key)
				zoom_usb=0
				

			

	if read6==0:
		touch=-1
		prev=-1
		read3=-1




