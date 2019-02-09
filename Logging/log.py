#coding:utf-8

'''
Created on 8 f�vr. 2019

@author: marti
'''
import os
import datetime
from time import sleep
# from urllib3.util.timeout import current_time
# from datetime import date

class mylog(object):
    '''
    classdocs
    '''


    def __init__(self, fileName, dateStamp=True):
        '''
        Constructor
        '''
        self.fileName = fileName
        self.dateStamp = dateStamp
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        self.fullFileName = currentTime + '_' + fileName + '.txt'
        with open(currentTime + '_' + fileName + '.txt', 'a') as fh:
            fh.write("File create\n")
        print(currentTime)
    
    def addLog(self, message):
        with open(self.fullFileName, 'a') as fh:
            currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            fh.write(currentTime + ': ' + message + '\n')
        print("add")
        
l = mylog('Martin')
l.addLog('AllO')

for i in range(10):
#     currentTime = datetime.datetime.now()
    l.addLog('Ecrit la ligne' + str(i))
    assert i != 5, 'Mauvaise valeur'
    sleep(0.1)
    
    
    
    
