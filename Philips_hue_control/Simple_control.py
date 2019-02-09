#!/usr/bin/python
from phue import Bridge, Light
from time import sleep

from tkinter import *




def listLumiere():
    lightsList = b.get_light_objects(mode='id')
    print(lightsList)
    
def colorLoop():
    """
    Red 1, orange 4000, yellow 10200, green 24000, Blue 45000, purple 52000
    """
    for i in range(0, 65535, 200):
       test_light.hue = i
       test_light.saturation = 200
       sleep(0.2)
       print(i)

def colorSwitch():
    lColor = [1, 4000, 10200, 24000, 45000, 52000]
    test_light.saturation = 254 
    for i in lColor:
        test_light.hue = i
        sleep(2)

def setBright():
    vvalue = w.get()
    test_light.brightness = vvalue
    





b = Bridge('10.0.0.2')
lights = b.lights

#listLumiere()

bureau1 = Light(b, 1)
bureau2 = Light(b, 2)
test_light = Light(b, 5)
test_light.on = False
test_light.on = True
test_light.brightness = 254
test_light.saturation = 254
#test_light.effect = "colorloop"
#colorLoop()
while (True):
    colorSwitch()

    
#bureau1.on = False
#bureau2.on = False

#bureau1.on = True
#bureau2.on = True

#bur1ColorMode = bureau1.colormode
#print(bur1ColorMode)
#bureau1.hue = 459 

#lightsList = b.get_light_objects(mode='id')
#print(lightsList)

# Print light names
#for l in lights:
#    print(l.name)

#b.set_light(['Hue color lamp 1','Hue color lamp 2'], 'bri', 254)
#b.set_light(['Hue color lamp 1','Hue color lamp 2'], 'ct', 250)

#bl = b.get_light_objects()


