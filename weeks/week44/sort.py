import random

def merge(lst0, lst1):
    """ Merge two sorted lists """
    newlst = []
    pos0, pos1 = 0, 0
    while pos0 < len(lst0) and pos1 < len(lst1):
        # Pick the smallest element (lst.pop(0) takes out element 0 from lst)
        if lst0[pos0] <= lst1[pos1]:
            newlst.append(lst0[pos0])
            pos0 += 1
        else:
            newlst.append(lst1[pos1])
            pos1 += 1
    # Append remaining elements (one of them may contain skipped elements)
    newlst += lst0[pos0:] + lst1[pos1:]
    return newlst

def mergesort(lst):
    """ Sort list using Merge Sort """
    if len(lst) <= 1: # List is already sorted
        return lst
    # Split list on mid and sort both parts
    L = len(lst)/2
    left, right = mergesort(lst[:L]), mergesort(lst[L:])
    # Merge the two sorted lists
    return merge(left, right)


def quicksort(lst):
    """ Sort list using Quick Sort """
    if len(lst) <= 1: # List is already sorted
        return lst
    pi = random.choice(range(len(lst)))
    pe = lst.pop(pi)
    lst0, lst1 = [], []
    for e in lst:
        if e < pe:
            lst0.append(e)
        else:
            lst1.append(e)
    return quicksort(lst0) + [pe] + quicksort(lst1)




# Test sorting functions
lst = range(20)
random.shuffle(lst)

print mergesort(lst)
print quicksort(lst)
