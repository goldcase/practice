#!/usr/bin/python

# kth smallest element is the minimum possible n such that there are atleast k elements in the array <= n.
# In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )

# quickselect

def partition(l, lo, hi, pivot_index):
    pivot_value = l[pivot_index]                  # store pivot value
    l[pivot_index], l[hi] = l[hi], l[pivot_index] # swap the two in a beautiful way
    wall = lo

    for i in range(lo, hi): # iterate through the whole array
        if l[i] < pivot_value:
            l[i], l[wall] = l[wall], l[i]
            wall += 1

    return l

lst = [5,1,9,3,8,5,3,2]

print(lst)
print(partition(0, len(lst) - 1, lst[5]))
    

