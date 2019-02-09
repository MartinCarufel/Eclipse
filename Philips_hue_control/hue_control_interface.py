'''
Created on Dec. 29, 2018

@author: Martin
'''
from tkinter import *
from phue import Bridge, Light

def set_values(value=None):
    test_light.brightness = sa1.get()

def set_temp(value=None):
    test_light.colortemp_k = sa2.get()

def turnOn():
    test_light.on = True

def turnOff():
    test_light.on = False

def switch():
    print('Light switch {}' .format(la1_var.get()))
    test_light.on = la1_var.get()
    
    set_scale_state()

def set_scale_state():
    state_test_light = test_light.on
    if state_test_light:
        sa1.config(state=NORMAL, fg='#000000')
        sa2.config(state=NORMAL, fg='#000000')
    else:
        sa1.config(state=DISABLED, fg='#808080')
        sa2.config(state=DISABLED, fg='#808080')

b = Bridge('10.0.0.2')
lights = b.lights
test_light = Light(b, 5)
light_a = Light(b, 5)
light_b = Light(b, 3)


#test_light.on = True
#test_light.colortemp_k = 3200

#test_light.brightness = 50

state_test_light_a = light_a.on
default_brightness_a = light_a.brightness
default_color_temp_a = light_a.colortemp_k

state_test_light_b = light_b.on
default_brightness_b = light_b.brightness
default_color_temp_b = light_b.colortemp_k

root=Tk()
la1_var=BooleanVar(None, state_test_light_a)
sa1_var = IntVar(None, default_brightness_a)
sa2_var = IntVar(None, default_color_temp_a)
sa1 = Scale(root, from_=0, to=254, orient=HORIZONTAL, variable=sa1_var, command=set_values)
sa2 = Scale(root, from_=2000, to=6500, orient=HORIZONTAL, variable=sa2_var, command=set_temp)

lb1_var=BooleanVar(None, state_test_light_b)
sb1_var = IntVar(None, default_brightness_b)
sb2_var = IntVar(None, default_color_temp_b)
sb1 = Scale(root, from_=0, to=254, orient=HORIZONTAL, variable=sb1_var, command=set_values)
sb2 = Scale(root, from_=2000, to=6500, orient=HORIZONTAL, variable=sb2_var, command=set_temp)


sa1.pack()
sa2.pack()
sb1.pack()
sb2.pack()

ra1=Radiobutton(text='On', variable=la1_var, value=True ,width=6, indicatoron=False, command=switch).pack(side='left')
ra2=Radiobutton(text='Off', variable=la1_var, value=False ,width=6, indicatoron=False, command=switch).pack(side='left')
rb1=Radiobutton(text='On', variable=lb1_var, value=True ,width=6, indicatoron=False, command=switch).pack(side='left')
rb2=Radiobutton(text='Off', variable=lb1_var, value=False ,width=6, indicatoron=False, command=switch).pack(side='left')

set_scale_state()

root.mainloop()