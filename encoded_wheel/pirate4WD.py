#! /usr/bin/python
#

import RPi.GPIO as GPIO
import time


pin = 40

def actualizar(pinx):
	time0 = time.time()

	GPIO.wait_for_edge(pinx, gpio.RISING)

	deltaT = time.time() - time0
	print("DTime = " + str(deltaT))

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pin, GPIO.IN)	#pull_up_down=GPIO.PUD_DOWN
	GPIO.add_event_detect(pin, GPIO.FALLING, callback=actualizar)	# add bounce time ?

	raw_input("")
