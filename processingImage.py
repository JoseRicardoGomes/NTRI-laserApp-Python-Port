import cv2 as cv
import numpy
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class processingImage:
		posX = 0
		posY = 0
		Hmin = 0
		Hmax = 180
		Smin = 0
		Smax = 255
		Vmin = 0
		Vmax = 255
		frameWidth = 1024
		frameHeight = 768
	
	def setCam(self):
		try:
			camera = PiCamera()
			camera.resolution = (frameWidth, frameHeight)
			camera.framerate = 32
			rawCapture = PiRGBArray(camera, size=(frameWidth, frameHeight))
		except RuntimeError:
			print("Unable to set up the camera, is it enabled in the raspi-config?")
	
	def getImg(self):

	def getImgTreshold(self):

	def setHSV(self, int Hmin, int Hmax, int Smin, int Smax, int Vmin, int Vmax):

	def getHSV(self):

	def setPosxPosy(self, int x, int y):

	def setImg(self);

	def morph(self);

	def trackObject(self);

	def drawObject(self);

	def __init__(self):
		setCam()
		getImg()
		getImgTreshold()
		setHSV()
		setPosxPosy(x,y)
		setImg()
		morph()
		trackObject()
		drawObject()

	
	def __del__(self):
		del rawCapture
	
		

