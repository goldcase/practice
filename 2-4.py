#!/usr/bin/python

from classes.LinkedList import *

linked_list = create_rand_list(15)

# Write code to partition a linked list around a value x

def partition_list(l, x):
    less    = LinkedList()
    greater = LinkedList()

    curr = l.head
    while curr.next != None:
        if curr.value < x:
            less.add_node(curr.value)
        else:
            greater.add_node(curr.value)
        curr = curr.next

    less.tail.next = greater.head
    less.tail = greater.tail
    
    return less

# test
print("Random Linked List: " + str(linked_list))
print("Partition around 0")
print(partition_list(linked_list, 0))
