#coding:utf-8
'''
Created on Dec. 31, 2018

@author: Martin
'''
from numpy.distutils.fcompiler import none
from _hashlib import new
from test.leakers import test_selftype
from numpy.core.defchararray import upper

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self._color = none
        self.id = none
        self.value = none
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = upper(value)
    

new_object = MyClass('martin')
new_object.color = 'rouge'
new_object.id = 12
new_object.value = 999
print("l'objet {0}, est de couleur {1}, son id est {2} et sa valeur est de {3}" .format(new_object.name, new_object.color, new_object.id, new_object.value))

