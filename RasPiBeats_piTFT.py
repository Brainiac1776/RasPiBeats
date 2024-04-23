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
size = width, height = 320, 240

pitft = pigame.PiTft()
lcd = pygame.display.set_mode(size)
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None,20)

WHITE = (255, 255, 255)

start_touch_buttons = {'Start': (150, 220)}

pygame.display.update()

level_one = True
level_two = False
level_three = False

while (1):
    pift.update()
    if (level_one):
        
    elif (level_two):
    
    elif (level_three):

pygame.display.quit()
pygame.quit()
del(pitft)