#!/usr/bin/python

from classes.LinkedList import *

dup = [9, 3, 6, 2, 1, 2, 8, 3, 7]

l_dup = create_linked_list(dup)

print(str(l_dup.head.value))
print(str(l_dup))

# Description: Removes duplicates from a linked list with a hash table
# param      : linked list with/without duplicates
# return     : purged linked list

def remove_dup(l):
    d = {}
    curr = l.head
    
    while curr.next != None:
        if curr.value in d:
            d[curr.value] += 1
        else:
            d[curr.value] = 1

        curr = curr.next

    for k in d:
        if d[k] > 1:
            for i in range(0, d[k] - 1):
                l.remove_node(k)
                print(str(l))
                d[k] -= 1

    return l

print(str(remove_dup(l_dup)))
