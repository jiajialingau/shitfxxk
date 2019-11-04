
import os
import sys
class Person:
    
    ##fuck off

    def __init__(self, firstname, lastname, score):
        self.firstname=firstname
        self.lastname=lastname
        self.score=score

    def Pr(self):
        os.system('cls')
        print('Student first name is: '+ self.firstname)
        print('Studnet last name is: ' + self.lastname)
        print('Student score is: ' + str(self.score))
               
             
    def grade(self):
        if self.score < 60:
            self.gradeTAG='fail'
            print ('grade is fail')
        elif self.score >= 60 and self.score<=80:
            self.gradeTAG='pass'
            print ('grade is pass')
        elif self.score >80 and self.score<=100:
            self.gradeTAG='good'
            print ('grade is good')
        else:
            print("That's not possible")



