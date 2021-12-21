# Copyright (c) ProSeg | programs
# Guess Game

import random

def init():
    print("Guess Game ...")
    try:
        rand = random.randint(0,10)
        inp = int(input("Guess of number : "))
        if inp == rand:print("You win !!!")
        else :print("You lose ...");print("It's was : "+str(rand)+" ...")
    except:pass
