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
font_L2 = pygame.font.Font(None, 50)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Instruments
#instruments = {'Bass Drum':(160, 220), 'Tom Tom':(160, 220), 'Hi hat':(160, 220), 'Cymbal':(160, 220), 'Crash Cymbal':(160, 220), 'Snare':(160, 220)}
instruments = ['Bass Drum', 'Tom Tom', 'Hi Hat', 'Cymbal', 'Crash Cymbal', 'Snare']
track_list = [1, 2, 3, 4, 5, 6, 7, 8]
track_list_index = 0

# touch buttons
start_touch_buttons = {'Start': (160, 20)}
level_two_buttons = {'Sound:' + instruments[track_list_index]:(160, 120), '<-': (120, 160), str(track_list[track_list_index]): (130, 160), '->': (140, 160), 'Go': (160, 160), 'Volume': (30, 50)}

# volume button
# volume_bar = pygame.draw.rect(lcd, RED, (160, 120, 15, 100), 0)

pygame.display.update()

level_one = True
level_two = False
level_three = False

#images
logo = pygame.image.load("RasPiBeats_logo.png")
logo = pygame.transform.scale(logo, (50,50))
logo_rect = logo.get_rect()


while (1):
    pift.update()
    if (level_one):
        print("Level One")
        lcd.fill((0,0,0))
        for k,v in start_touch_buttons.items():
            text_surface = font_big.render('%s'%k, True, WHITE)
            rect = text_surface.get_rect(center=v)
            lcd.blit(text_surface,rect)
        logo_rect.center(160,120)
        for event in pygame.event.get():
            if (event.type is MOUSEBUTTONDOWN):
                x,y = pygame.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                x,y = pygame.get_pos()
                if y > 200 and (x > 120 and x < 200):
                    level_two = True
                    level_one = False
        
    elif (level_two):
        print("Level Two")
        lcd.fill((0,0,0))
        for k,v in level_two_buttons.items():
            text_surface = font_L2.render('%s'%k, True, WHITE)
            rect = text_surface.get_rect(center=v)
            lcd.blit(text_surface,rect)
        pygame.draw.rect(lcd, RED, (160, 120, 15, 100), 0)
        for event in pygame.event.get():
            if (event.type is MOUSEBUTTONDOWN):
                x,y = pygame.get_pos()
            elif(event.type is MOUSEBUTTONUP):
                x,y = pygame.get_pos()
                print(x,y)
    
    elif (level_three):

pygame.display.quit()
pygame.quit()
del(pitft)