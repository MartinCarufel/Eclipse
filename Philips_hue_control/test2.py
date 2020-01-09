#coding:utf-8

from phue import Bridge, Light
from time import sleep
from tkinter import *
from PIL.ImageChops import lighter

class Light_control(Light, Button):
    '''
    classdocs
    '''


    def __init__(self, bridge, light_id, master):
        '''
        Constructor
        '''
        Light.__init__(self, bridge, light_id)
        Button.__init__(self, master)
        
        #self.on_off()
        
        #Tk.__init__(self)
        #self.state_light = self.on
        self.default_brightness = self.brightness
        self.default_color_temp = self.colortemp_k
        self.master = master
        
        self.lstate_var = BooleanVar(None, self.on)
        self.s1_var = IntVar(None, self.default_brightness)
        self.s2_var = IntVar(None, self.default_color_temp)
        self.s1 = Scale(root, from_=0, to=254, orient=HORIZONTAL, variable=self.s1_var, command=self.set_values)
        self.s2 = Scale(root, from_=2000, to=6500, orient=HORIZONTAL, variable=self.s2_var, command=self.set_temp)
        
        self.s1.pack()
        self.s2.pack()
#         r1=Radiobutton(text='On', variable=lstate_var, value=True ,width=6, indicatoron=False, 
#                        command=self.switch_on).pack(side='left')
#         r2=Radiobutton(text='Off', variable=lstate_var, value=False ,width=6, indicatoron=False, 
#                        command=self.switch_off).pack(side='left')
                       
        self.r1=Radiobutton(text='On', variable=self.lstate_var, value=True ,width=6, indicatoron=False, 
                       command=self.switch_on).pack()
        self.r2=Radiobutton(text='Off', variable=self.lstate_var, value=False ,width=6, indicatoron=False, 
                       command=self.switch_off).pack()
        
        self.set_scale_state()
        
       
        
    def print_all(self):
        print("State: {}, Brightness: {}, Color Temp: {}" .format(
        self.state_light, self.default_brightness, self.default_color_temp,))
    
    def set_scale_state(self):
        print('set scale')
        self.lstate_var = self.on
        if self.lstate_var:
            print('lstate True')
            self.s1.config(state=NORMAL, fg='#000000')
            self.s2.config(state=NORMAL, fg='#000000')
        else:
            print('lstate Else')
            self.s1.config(state=DISABLED, fg='#808080')
            self.s2.config(state=DISABLED, fg='#808080')
    
    def set_temp(self, value=None):
        self.colortemp_k = self.s2_var.get()
    
    def set_values(self, value=None):
        self.brightness = self.s1_var.get()
    
    def switch_on(self):
        self.on = True
        self.set_scale_state()
        
    def switch_off(self):
        self.on = False
        self.set_scale_state()
    
    def on_off(self):
        self.on = True
        sleep(2)
        self.on = False

root = Tk()  
b = Bridge('10.0.0.2')     
a = Light_control(b, 5, root)
x = Light_control(b, 4, root)
y = Light_control(b, 3, root)


# a.on = True
# sleep(1)
# a.brightness = 100
# a.print_all()
# sleep(3)


a.mainloop()

a.on = False
x.on = False


        
