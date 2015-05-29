#!/usr/bin/python

from classes.LinkedList import *

linked_list = create_rand_list(15)

# Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next
    return

start = linked_list.head
trail = linked_list.head

interval = 0
while start.next != None:
    start = start.next
    if (interval == 2):
        trail = trail.next
        interval = 0
    interval += 1

print("Random Linked List: " + str(linked_list))
print("Middle Node value: " + unicode(trail))
delete_middle_node(trail)
print("New List: " + str(linked_list))
