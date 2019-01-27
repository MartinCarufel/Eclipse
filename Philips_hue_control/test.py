#coding:utf-8
'''
Created on Dec. 29, 2018

@author: Martin
'''


from phue import Bridge, Light, AllLights, Group
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

# test_light.on = False
# sleep(2)
# test_light.on = True
# sleep(2)
# test_light.on = False
# sleep(2)
print(b.groups)

nb_group = b.groups
#print(len(nb_group))

print(b.get_group_id_by_name('control_group'))

#print(b.lights)

#b.create_group('control_group', [3, 4, 5])
b.set_group(group_id='control_group', parameter='lights', value=[5])

gr0 = Group(b, 'control_group')
gr0.on = True
gr0.brightness = 254
gr0.colortemp_k = 3500
sleep(3)
gr0.on = False
b.set_group(group_id='control_group', parameter='lights', value=[3, 4])

gr0 = Group(b, 'control_group')
gr0.on = True
gr0.brightness = 254
gr0.colortemp_k = 3500
sleep(3)
gr0.on = False
# print(b.get_group_id_by_name('control_group'))



print(b.groups)

# b.create_group('control_group', [5])
# gr0 = Group(b, 'control_group')
# sleep(1)
# gr0.on = True
# gr0.brightness = 254
# gr0.colortemp_k = 3500
# sleep(3)
# gr0.on = False

#colorChange(0, 3, color)
#flash(0.1, 0.1, 100)
# test_light.on = True
# test_light.colortemp_k = 3300
# test_light.brightness = 50
# test_light.transitiontime = 2
# test_light.on = True
# sleep(3)
# test_light.brightness = 100
# sleep(1)
# test_light.brightness = 0
# sleep(3)
# test_light.on = False