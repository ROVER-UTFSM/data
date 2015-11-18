#! /usr/bin/python
#

import RPi.GPIO as GPIO
import time


pin = 12
estado = 0
time0  = 0

def actualizar(pinx):
	time1 = time.time() - time0
	print("DTime = " + str(time1))
	time0 = time1

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pin, GPIO.IN)	#pull_up_down=GPIO.PUD_DOWN
	GPIO.add_event_detect(pin, GPIO.FALLING, callback=actualizar)	# add bounce time ?

	raw_input("")
