#!/usr/bin/python

# kth smallest element is the minimum possible n such that there are atleast k elements in the array <= n.
# In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )

# quickselect

def partition(l, lo, hi, pivot_index):
    pivot_value = l[pivot_index]                  # store pivot value
    l[pivot_index], l[hi] = l[hi], l[pivot_index] # swap the two in a beautiful way
    wall = lo                                     # marks the wall between less than and (greater than || equal to)

    for i in range(lo, hi):               # iterate through the whole array
        if l[i] < pivot_value:            # if this value is less than the pivot value,
            l[i], l[wall] = l[wall], l[i] # swap it with the value at the wall index
            wall += 1                     # and move the wall up to "protect" the partitioned values

    l[wall], l[hi] = l[hi], l[wall]       # swap pivot with wall to mark the divide

    return l

lst = [5,1,9,3,8,5,3,2]

print(lst)
print("Partitioning lst around " + str(lst[5]))
print(partition(lst, 0, len(lst) - 1, lst[5]))

lst_2 = [10, 100, 30, 21, 52, 77, 11, -19, 49, 62, 0]
print(lst_2)
print("Partitioning lst_2 around 21")
print(partition(lst_2, 0, len(lst_2) - 1, 3))
