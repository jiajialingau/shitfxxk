import os
import sys
import airplane

os.system('cls')
planename=input("Please input air plane name: ")
os.system('cls')
planemodel=input("Please input air plane model: ")
os.system('cls')
planereg=input("Please input air plane reg number: ")


myplane = airplane.airplane(planename,planemodel,planereg)
myplane.display()

myplane.takeoff()

##shut the fuxk off

