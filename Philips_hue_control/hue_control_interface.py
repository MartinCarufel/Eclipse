'''
Created on Dec. 29, 2018

@author: Martin
'''
from tkinter import *
from phue import Bridge, Light

def set_values(value=None):
    test_light.brightness = s1.get()

def set_temp(value=None):
    test_light.colortemp_k = s2.get()

def turnOn():
    test_light.on = True

def turnOff():
    test_light.on = False
    

b = Bridge('10.0.0.2')
lights = b.lights
test_light = Light(b, 5)
test_light.colortemp_k = 3800
test_light.on = True

root=Tk()

s1 = Scale(root, from_=0, to=254, orient=HORIZONTAL, command=set_values)
s2 = Scale(root, from_=2000, to=6500, orient=HORIZONTAL, command=set_temp)
#                                                ^^^^^^^^^^^^^^^^^^^
#s1.set(19)
s1.pack()
s2.pack()

Button(root, text='On', command=turnOn).pack()
Button(root, text='Off', command=turnOff).pack()
root.mainloop()