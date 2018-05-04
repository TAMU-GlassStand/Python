#!/usr/bin/python

import RPi.GPIO as gpio
import time

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

LED1=0
LED2=0
LED3=0
LED4=0
LED5=0

def led1(self):
	LED1=gpio.input(channel_1)

def led2(self):
	LED1=gpio.input(channel_2)

def led3(self):
	LED1=gpio.input(channel_3)

def led4(self):
	LED1=gpio.input(channel_4)

def led5(self):
	LED1=gpio.input(channel_5)



def read_gpio(self):
	LED1=gpio.input(channel_1)
	LED2=gpio.input(channel_2)
	LED3=gpio.input(channel_3)
	LED4=gpio.input(channel_4)
	LED5=gpio.input(channel_5)

	LED_code = [LED5, LED4, LED3, LED2, LED1]
	print "LED values : %s" % LED_code
	


if gpio.add_event_detect(channel_1, gpio.RISING, callback=read_gpio, bouncetime=1000):
	print"channel 1"
	read_gpio
elif gpio.add_event_detect(channel_2, gpio.RISING, callback=read_gpio, bouncetime=1000):
	print"channel 2"
	read_gpio
while 1:
	LED_code = [LED5, LED4, LED3, LED2, LED1]
	print "LED values : %s" % LED_code
	time.sleep(1)






