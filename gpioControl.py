##***********************************************************
##Universidade Lusiada de VN de Famalicão                    *
##NTRI - tracking camera Proof Of Concept                    *
##Python build 0.0.0                                         *
##2016-2017                                                  *
##                                                           *
##By: Filipe Santos and JRG                                  *
##***********************************************************/

try:
import RPi.GPIO as GPIO
except RuntimeError:
	print("Unable to import the GPIO module, try to run this as super user")

import time

#the pins that that control the coils of the base stepper
pin11 = 11
pin12 = 12
pin13 = 13
pin15 = 15

#the coils that control the coils of the camera stepper
pin29 = 29
pin31 = 31
pin33 = 33
pin35 = 35

#Setup funcs-----------------------------------------------------------------------------------------------------------------------------
#setup the pins as board
def setMode():
	print("Setting the rpi GPIO mode as board...")
	try:
	gpio.setmode(gpio.board)
	except RuntimeError:
		print("Unable to set as board. The GPIO lib hasn't been imported or your board is defective. Send your complains to /dev/null")
	else:
	print("GPIO set as board with the pin numbers: 11,12,13,14,29,31,33,35")
#set the mode of the base stepper pins
def setGPIOpinModeBase():
	try:
	gpio.setup(pin11,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #11")
	try:
	gpio.setup(pin12,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #12")
	try:
	gpio.setup(pin13,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #13")
	try:
	gpio.setup(pin15,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #15")
	else:
		print("GPIO 11,12,13,15 sucefully set to out")
#setup the mode of the camera stepper pins
def setGPIOpinModeCamera():
	try:
	gpio.setup(pin29,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #29")
	try:
	gpio.setup(pin31,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #31")
	try:
	gpio.setup(pin33,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #33")
	try:
	gpio.setup(pin35,gpio.OUT)
	except RuntimeError
		print("Unable to set the pin #35")
	else:
		print("GPIO 11,12,13,15 sucefully set to out")
#END setup funcs--------------------------------------------------------------------------------------------------------------------------------------

def step1(int pin1, int pin2, int pin3, int pin4):
	GPIO.output(pin1, HIGH)
	GPIO.output(pin2, HIGH)
	GPIO.output(pin3, HIGH)
	GPIO.output(pin4, HIGH)
def step2(int pin1, int pin2, int pin3, int pin4):
	GPIO.output(pin1, HIGH)
	GPIO.output(pin2, HIGH)
	GPIO.output(pin3, HIGH)
	GPIO.output(pin4, HIGH)
def step3(int pin1, int pin2, int pin3, int pin4):
	GPIO.output(pin1, HIGH)
	GPIO.output(pin2, HIGH)
	GPIO.output(pin3, HIGH)
	GPIO.output(pin4, HIGH)
def step4(int pin1, int pin2, int pin3, int pin4):
	GPIO.output(pin1, HIGH)
	GPIO.output(pin2, HIGH)
	GPIO.output(pin3, HIGH)
	GPIO.output(pin4, HIGH)

def sequenceLeft(int pin1, int pin2, int pin3, int pin4):
	step1(pin1, pin2, pin3, pin4)
	step2(pin1, pin2, pin3, pin4)
	step3(pin1, pin2, pin3, pin4)
	step4(pin1, pin2, pin3, pin4)

def sequenceRight(int pin1, int pin2, int pin3, int pin4):
	step4(pin1, pin2, pin3, pin4)
	step3(pin1, pin2, pin3, pin4)
	step2(pin1, pin2, pin3, pin4)
	step1(pin1, pin2, pin3, pin4)

def fullReset(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6, int pin7, int pin8):
	GPIO.output(pin1, LOW)
	GPIO.output(pin2, LOW)
	GPIO.output(pin3, LOW)
	GPIO.output(pin4, LOW)
	GPIO.output(pin5, LOW)
	GPIO.output(pin6, LOW)
	GPIO.output(pin7, LOW)
	GPIO.output(pin8, LOW)