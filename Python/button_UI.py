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


busnum=1
address=0x0a
offset=0x00
data0=[0, 0, 0, 0, 0, 0]
bus=SMBus(busnum)
b=bus.read_byte_data(address,offset)
print b


prev=-1
file_sel=-1
user_location=-1 # Used to determine where the user is: 0=Settings, 1=Google Drive, 2=Removeable Storage

#Google Drive Variables
n_pdf=0
scale_pdf=3.65 #Multiplier used for scrolling
base_pdf=6 # Base Y mulitplier
x_pdf=x_pos*26
y_pdf=y_pos*6


# Removable Storage Variables
n_usb=0
scale_usb=1.675 #Multiplier used for scrolling
base_usb=10 # Base Y multiplier
x_usb=x_pos*25
y_usb=y_pos*10


while 1:
	
	bus.write_i2c_block_data(0x0a, 0x00, data0) #Write which sensor element looking for (buttons)
	read=bus.read_i2c_block_data(address, 0, 6)
	read1=read[0] #Byte 1
	read2=read[1] #Byte 2
	read3=read[2] #Byte 3 (Changes based on button being pressed)
	read4=read[3] #Byte 4
	read5=read[4] #Byte 5
	read6=read[5] #Byte 6 (Changes when touch/proximity is detected)

	touchbit=read6 & 0x01

	if touchbit==1 and read3!=prev:
		prev=read3
		touchbit=-1

		if read3==0:
			print"Button 1 was pressed"

			# Settings
			m.move(x_pos*9, y_pos*15)
			m.click(x_pos*9, y_pos*15, 1)
			user_location=0	#Flag so buttons 2 and 3 only click if on the settings page		

			#Clear scrolling count
			n_usb=0
			n_pdf=0

		elif read3==1:
			print"Button 2 was pressed"

			if user_location==0:
				# Brightness Plus
				m.move(x_pos*30, y_pos*21.25)
				m.click(x_pos*30, y_pos*21.25, 1)

				# Apply Changes  
				m.move(x_pos*26, y_pos*22.5)
				m.click(x_pos*26, y_pos*22.5, 1)

				#Clear scrolling count 
				n_usb=0
				n_pdf=0

		elif read3==2:
			print"Button 3 was pressed"

			if user_location==0:
				# Brightness Minus
				m.move(x_pos*35.25, y_pos*21.25)
				m.click(x_pos*35.25, y_pos*21.25, 1)

				# Apply Changes
				m.move(x_pos*26, y_pos*22.5)
				m.click(x_pos*26, y_pos*22.5, 1)

				#Clear scrolling count
				n_usb=0
				n_pdf=0

		elif read3==3:
			print"Button 4 was pressed"
			
			# Google Drive
			m.move(x_pos*9, y_pos*45)
			m.click(x_pos*9, y_pos*45, 1)
			user_location=1
			time.sleep(1)
			m.move(x_pdf, y_pdf)

			#Clear scrolling count
			n_usb=0
			n_pdf=0

		elif read3==4:
			print"Button 5 was pressed"

			# Up 
			if user_location==1:
				n_pdf=n_pdf-1
				m.move(x_pdf, y_pos*(base_pdf+n_pdf*scale_pdf))
			
			elif user_location==2:
				n_usb=n_usb-1
				m.move(x_usb, y_pos*(base_usb+n_usb*scale_usb))

				
		elif read3==5:
			print"Button 6 was pressed"

			# Down
			if user_location==1:
				n_pdf=n_pdf+1
				m.move(x_pdf, y_pos*(base_pdf+n_pdf*scale_pdf))

			elif user_location==2:
				n_usb=n_usb+1
				m.move(x_usb, y_pos*(base_usb+n_usb*scale_usb))
				
		elif read3==6:
			print"Button 7 was pressed"

			# Removable Storage
			m.move(x_pos*9, y_pos*80)
			m.click(x_pos*9, y_pos*80)
			user_location=2
			time.sleep(1)
			m.move(x_usb, y_usb)

			#Clear scrolling count
			n_usb=0
			n_pdf=0
			

		elif read3==7:
			print"Button 8 was pressed"
		elif read3==8:
			print"Button 9 was pressed"
			if user_location==1:
				m.click(x_pdf, y_pdf, 1)
			
			elif user_location==2:
				m.click(x_usb, y_usb, 1)

	if read6==0:
		touch=-1
		prev=-1
		read3=-1




