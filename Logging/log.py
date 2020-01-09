#coding:utf-8

'''
Created on 8 f�vr. 2019

@author: martin
'''
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
        if dateStamp:
            currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
            self.fullFileName = currentTime + '_' + fileName + '.txt'
            
        else:
            self.fullFileName = fileName + '.txt'
        with open(self.fullFileName, 'w'):
            pass
    
    def addLog(self, message):
        with open(self.fullFileName, 'a') as fh:
            currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            fh.write(currentTime + ': ' + message + '\n')
        
l = mylog('Martin', False)
l.addLog('AllO')

for i in range(10):
    l.addLog('Ecrit la ligne' + str(i))
    #assert i != 5, 'Mauvaise valeur'
    sleep(0.1)
    
    
    
    
