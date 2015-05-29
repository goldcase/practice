# Description: class of linked list node

import random

class Node:
    """A simple node class for a linked list"""

    def __init__(self, value):
        self.value = value # instance variables
        self.next = None

    def __unicode__(self):
        return self.value

# Description: class of LinkedList
#            : construct empty or with list or another LinkedList
#            : can add and remove nodes

class LinkedList:
    """A simple class for a linked list"""

    # empty initialization
    def __init__(self):
        self.head = None
        self.tail = None

    # add a node to the linked list
    def add_node(self, val):
        node = Node(val)
        if self.head == None: # case: list is empty
            self.head = node
            self.tail = node
        else: # case: nonempty list
            self.tail.next = node
            self.tail = node

        return

    # remove node with value equal to node_val
    def remove_node(self, node_val):
        prev = self.head
        curr = self.head
        
        while curr.next != None:
            prev = curr
            curr = curr.next
            if curr.value == node_val:
                prev.next = curr.next
                break

        return

    def __unicode__(self):
        ret = []
        curr = self.head
        
        while curr.next != None:
            ret.append(curr.value)
            curr = curr.next

        return str(ret)

    def __str__(self):
        return unicode(self).encode('utf-8')

def create_linked_list(l):
    linked_list = LinkedList()
    for item in l:
        linked_list.add_node(item)

    return linked_list

# param : n items in list
# return: linked list with n nodes of random ints between -100 and 100

def create_rand_list(n):
    rand_list = []
    for i in xrange(n):
        rand_list.append(random.randint(-100,100))
    linked_list = create_linked_list(rand_list)

    return linked_list
    

