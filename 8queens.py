# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:07:01 2015
8 queens solver
@author: Matthew Vander Hoff
"""
import random


n = 8
solutions = []
current = []

def place(col):
    possible = []
    attacks = []
    for x in current:
        attacks.append(x+col)
        attacks.append(x-col)
    for x in range(n):
        if x not in current:
            if x not in attacks:
                possible.append(x)
    return possible

def start():
    for x in range(n):
        place(x)