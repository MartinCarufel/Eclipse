#coding:utf-8

from phue import Bridge, Light
from time import sleep
from tkinter import *
from PIL.ImageChops import lighter

class Light_control(Light, Button):
    '''
    classdocs
    '''


    def __init__(self, bridge, light_id, master, pos_row, pos_col):
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
        self.default_hue = self.hue
        self.default_saturation = self.saturation
        self.master = master
        
        self.lstate_var = BooleanVar(None, self.on)
        self.s1_var = IntVar(None, self.default_brightness)
        self.s2_var = IntVar(None, self.default_color_temp)
        self.s3_var = IntVar(None, self.default_hue)
        self.s4_var = IntVar(None, self.default_saturation)
        self.s1 = Scale(root,  label='Brightness', from_=0, to=254, orient=HORIZONTAL, variable=self.s1_var, command=self.set_values)
        self.s2 = Scale(root,  label='Color temp', from_=2000, to=6500, orient=HORIZONTAL, variable=self.s2_var, command=self.set_temp)
        self.s3 = Scale(root,  label='Hue', from_=0, to=65535, orient=HORIZONTAL, variable=self.s3_var, command=self.set_hue)
        self.s4 = Scale(root,  label='Saturation', from_=0, to=254, orient=HORIZONTAL, variable=self.s4_var, command=self.set_saturation)
        
#         self.s1.pack()
#         self.s4.pack()
#         self.s2.pack()
#         self.s3.pack()
        self.s1.grid(row=pos_row, column=pos_col)
        self.s2.grid(row=pos_row+1, column=pos_col)
        self.s3.grid(row=pos_row, column=pos_col+1)
        self.s4.grid(row=pos_row+1, column=pos_col+1)
        
#         r1=Radiobutton(text='On', variable=lstate_var, value=True ,width=6, indicatoron=False, 
#                        command=self.switch_on).pack(side='left')
#         r2=Radiobutton(text='Off', variable=lstate_var, value=False ,width=6, indicatoron=False, 
#                        command=self.switch_off).pack(side='left')
                       
        self.r1=Radiobutton(text='On', variable=self.lstate_var, value=True ,width=6, indicatoron=False, 
                       command=self.switch_on).grid(row=pos_row+2, column=pos_col)
        self.r2=Radiobutton(text='Off', variable=self.lstate_var, value=False ,width=6, indicatoron=False, 
                       command=self.switch_off).grid(row=pos_row+2, column=pos_col+1)
        
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
            self.s3.config(state=NORMAL, fg='#000000')
            self.s4.config(state=NORMAL, fg='#000000')
        else:
            print('lstate Else')
            self.s1.config(state=DISABLED, fg='#808080')
            self.s2.config(state=DISABLED, fg='#808080')
            self.s3.config(state=DISABLED, fg='#808080')
            self.s4.config(state=DISABLED, fg='#808080')
    
    def set_temp(self, value=None):
        self.colortemp_k = self.s2_var.get()
        
    def set_hue(self, value=None):
        self.hue = self.s3_var.get()
    
    def set_saturation(self, value=None):
        self.saturation = self.s4_var.get()
    
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
a = Light_control(b, 5, root, 0, 0)
x = Light_control(b, 4, root, 3, 0)
y = Light_control(b, 3, root, 0, 3)


# a.on = True
# sleep(1)
# a.brightness = 100
# a.print_all()
# sleep(3)


a.mainloop()

a.on = False
x.on = False


        
