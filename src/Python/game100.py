# A game to guess a number, with only 100 characters of code, including spaces
import random as r
x=r.randint(1,99)
y=0
while y!=x:
 y=int(input())
 if y>x:print("V")
 if y<x:print("^")
