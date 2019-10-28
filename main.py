
import os
import sys
import Person

os.system('cls')
Fname=input("Please input studnet first name: ")
os.system('cls')
Lname=input("Please input student Last name: ")
os.system('cls')
Score=input("Please input student score: ")
Score=int(Score)

stu1 = Person.Person(Fname,Lname,Score)

stu1.Pr()
stu1.grade()