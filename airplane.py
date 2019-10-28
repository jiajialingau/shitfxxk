
import os
class airplane:
    
    def __init__(self, planename,planemodel,planereg):
        self.planename=planename
        self.planemodel=planemodel
        self.planereg=planereg
        
        
    def display(self):
        print ("Air Plane name is: "+self.planename)
        print ("Air Plane model is: "+self.planemodel)
        print ("Air Plane Reg number is: "+self.planereg)
    
    
    def takeoff(self):
        print (self.planename+" of "+self.planemodel+" is taking off now!")
        
        
    
    
    
    
        