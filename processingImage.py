import cv2 as cv
import numpy as np
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

	#this function does the morphology of the image for better contour defenition
	#and noise cancelation
	def morph(self);
		erodeElement = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
		dilateElement = cv.getStructuringElement(cv.MORPH_RECT, (8,8))

		imgKernel_erosion = np.ones((3,3), np.uint8)
		cv.erode(rawCapture, imgKernel_erosion, iterations = 1)

		imgKernel_dilation = np.ones((8,8), np.uint8)
		cv.dilate(rawCapture, imgKernel_dilation, iterations = 1)

	def trackObject(self);
		cv.findContours(getImgTreshold, contours, hierarchy, CV_RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)

		boundRect(contours.size())

		
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
	
		

