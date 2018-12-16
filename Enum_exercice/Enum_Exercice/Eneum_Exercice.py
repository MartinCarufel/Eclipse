'''
Created on 11 nov. 2018

@author: marti
'''
from enum import Enum
from multiprocessing.managers import State

class Bug_state(Enum):
    '''
    classdocs
    '''
    New = 1
    Accepted = 2
    Progress = 3
    Test = 4
    Close = 5
    
class Bug():
    def __init__(self, xstate):
        self.xstate = xstate
    
    def next_step(self):
        self.xstate =+ 1
        #self.xstate += 1
    
    def previous_state(self):
        self.xstate -= 1
        #self.xstate -= 1
            
    
#print(Bug_state.New.value)
#print(Bug_state.New.name)

new_b = Bug(Bug_state.New)
print(new_b.xstate.name)
new_b.next_step()
print(new_b.xstate.value)

# new_b = Bug(1)
# print(new_b.xstate)
# new_b.next_step()
# print(new_b.xstate)