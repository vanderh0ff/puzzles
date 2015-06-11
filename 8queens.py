# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:07:01 2015
8 queens solver
@author: Matthew Vander Hoff
"""

board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

def check(x, y):
    # check row
    for x1 in range(8):
        if board[y][x1] == 1 : return False
    # check col
    for y1 in range(8):
        if board[y1][x] == 1 : return False
    # check diags
    #for daig in range(8):
        #if board[][] == 1 : return False:
    return True
    
def drawDiag(x,y):
    diags = []
    for u in range(8):
        if (x+u <= 8 and y-u >= 0):
            diags.add((x+u, y-u))
        if (x-u >= 0 and y-u >= 0):
            diags.add(x-u, y-u)

def place(x,y):
    pass
