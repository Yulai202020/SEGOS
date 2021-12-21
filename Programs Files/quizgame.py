# Copyright (c) ProSeg | programs
# Quiz Game

def init():

    print("Quiz :")
    source=0;total_questions=3

    answer=input("Question Math 1 : 100 / 4 * 2 # ")
    if answer.lower()=="50":
        source += 1;print("Correct !!!")
    else:print("Wrong Answer ...")

    answer=input("Question Math 2 : 10 ** 2 / 1 # ")
    if answer.lower()=="100":
        source += 1;print("Correct !!!")
    else:print("Wrong Answer ..")

    answer=input("Question Marh 3 : tg (30) ( sin (30) / cos(30) ) # ")
    if answer.lower()=="0.6":
        source += 1;print("Correct !!!")
    else:print("Wrong Answer ...")

    print("source :",source)
    mark=(source/total_questions)*100
    print("Marks obtained :",round(mark,2),"%")