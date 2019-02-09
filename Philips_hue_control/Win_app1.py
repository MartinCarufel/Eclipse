#coding:utf-8

from tkinter import *
from distutils import command
from phue import Bridge, Light

def switch():
    print('Light switch {}' .format(check_on.get()))
    test_light.on=check_on.get()
    
b = Bridge('10.0.0.2')
lights = b.lights
test_light = Light(b, 5)


root = Tk()
check_on = BooleanVar()
b1 = Button(root, text='On / Off', command=switch).pack()
b2 = Checkbutton(root, text='check', command=switch, onvalue=True, offvalue=False, variable=check_on, 
                 image='off_button.png', selectimage='on_button.png').pack()

root.mainloop()
