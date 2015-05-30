#!/usr/bin/python

from classes.LinkedList import *

# 819 + 251 == 1070
# reverse: 0701
reverse_add_1 = [9,1,8]
reverse_add_2 = [1,5,2]

def reverse_add(a, b):
    # assume same length
    curr_a = a.head
    while curr_a.next != None:

