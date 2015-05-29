#!/usr/bin/python

from classes.LinkedList import *

linked_list = create_rand_list(15) # create a linked list of random values with length 15

# Implement an algorithm to find the kth to last element of a SLL

def find_kth(l, k):
    start = l.head
    trail = l.head
    count = 0

    while start.next != None:
        start = start.next
        if count >= k:
            trail = trail.next
        count += 1

    return trail.value

print("Random list: " + str(linked_list))
print("Find 3rd to last element")
print(find_kth(linked_list, 3))
