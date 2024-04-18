import pygame, pigame  # Import pygame graphics library
from pygame.locals import *
import os # for OS calls
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
#need a quit button

//piTFT display stuff
# os.putenv('SDL_VIDEODRIVER','fbcon') # Display on piTFT
# os.putenv('SDL_FBDEV','/dev/fb1')
# os.putenv('SDL_MOUSEDRV','dummy')
# os.putenv('SDL_MOUSEDEV','/dev/null')
# os.putenv('DISPLAY','')

pygame.init()

pygame.mouse.set_visible(False)