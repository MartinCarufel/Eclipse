#coding:utf-8
'''
Created on Dec. 29, 2018

@author: Martin
'''


from phue import Bridge, Light
from time import sleep, time

def set_values(value=None):
    slider1 = s1.get()
    test_light.brightness = slider1
    #print(s1.get(), s2.get())
    print(slider1)

def set_temp(value=None):
    slider2 = s2.get()
    test_light.colortemp_k = slider2
    #print(s1.get(), s2.get())
    print(slider2)

def turnOn():
    test_light.on = True

def turnOff():
    test_light.on = False
    
def colorChange(t_time, steady_time, color_list):
    
    test_light.on = True
    test_light.brightness = 254
    test_light.saturation = 254
    test_light.transitiontime = t_time*10
    test_light.on = True
    for i in color_list:
        print("Couleur: {}" .format(i))
        test_light.hue = i
        sleep(t_time+steady_time)
    test_light.transitiontime = 0
    test_light.on = False

def flash(on_time, off_time, nb_flash):
    test_light.on = True
    test_light.brightness = 254
    test_light.saturation = 254
    test_light.transitiontime = 0
    sleep(2)
    x = time()
    for i in range(nb_flash):
        test_light.brightness = 254
        sleep(on_time)
        test_light.brightness = 0
        sleep(off_time)
    y = time()
    print(y-x)
b = Bridge('10.0.0.2')
lights = b.lights
test_light = Light(b, 5)
color = [1, 6000, 12000, 18000, 24000, 30000, 36000, 42000, 48000, 52000]
#colorChange(0, 3, color)
flash(0.1, 0.1, 100)