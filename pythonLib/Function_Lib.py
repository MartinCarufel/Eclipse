import sys
import datetime
import time
from distutils.file_util import write_file

class Function_Lib():

    def test1(self):
#         l = ['a', 'b', 'c']
#         try:
#             x = l[3]
#             
#         except:
#             raise 'Ca va mal'
        if(True):
            raise Exception('bad command')
            
        
    
    def greet_person(self, sPersonName):
        """
        says hello
        """
        if sPersonName == "Robert":
            raise Exception("we don't like you, Robert")
        print ("Hi there {0}".format(sPersonName))
    
    def print_screen(self, text):
        sys.stderr.write('{}\n' .format(text))
        
    def additionne(self, *arg):
        x = 0
        for i in arg:
            try:
                x = x + i
            except TypeError:
                sys.stderr.write('Could not add string, use ${value}')
                x = 0
                break
        return x    
    
    def Create_Log_File(self):
        name = time.strftime('%Y%m%d_%H%M%S') + '_LOG.txt'
        oFile = open(name, 'w',)
        return oFile
        
    def Add_To_File(self,fileobj, text):
        fileobj.write(text)
    
#test1()

# result = additionne(3, 't')
#name = datetime.datetime.now()
#name = time.strftime('%Y%m%d_%H%M%S')
#print(name)

#myFile = Create_Log_File()
#Add_To_File(myFile, 'Bonjour')

# greet_person("Robert")
# somme = additionne(2 ,3)
# print(somme)