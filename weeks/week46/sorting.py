# -*- coding: utf-8 -*-

import random, timing, sorting

random.seed(42)


def bubble_sort(lst):
    ''' Sorter med Bubble Sort '''
    n = len(lst)
    swap = True
    while swap:
        swap = False
        for i in xrange(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
        n = n - 1

def insertion_sort(lst):
    ''' Sorter liste med Insertion Sort '''
    sorted_lst = [lst.pop()]
    for elem in lst:
        i = 0
        while elem > sorted_lst[i]:
            i += 1
            if i == len(sorted_lst):
                break
        sorted_lst.insert(i, elem)


def merge(lst0, lst1):
    ''' Merge / Flet to lister '''
    newlst = []
    pos0, pos1 = 0, 0
    while pos0 < len(lst0) and pos1 < len(lst1):
        if lst0[pos0] <= lst1[pos1]:
            newlst.append(lst0[pos0])
            pos0 += 1
        else:
            newlst.append(lst1[pos1])
            pos1 += 1
    newlst += lst0[pos0:] + lst1[pos1:]
    return newlst

def merge_sort(lst):
    ''' Sorter liste med Merge Sort '''
    if len(lst) <= 1:
        return lst
    L = len(lst)/2
    left, right = merge_sort(lst[:L]), merge_sort(lst[L:])
    return merge(left, right)


def quick_sort(lst):
    ''' Sorter liste med Quick Sort '''
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
    return quick_sort(lst0) + [pe] + quick_sort(lst1)


def builtin_sort(lst):
    ''' Sorter liste med den indbyggede sort()  '''
    lst.sort()


def sort(algo, n):
    ''' Sorter en tilfældig liste af størrelse n med algo  '''
    # Lav tilfældig liste
    lst = random.sample(xrange(n**2), n)

    # Liste over mulige algoritmer
    algorithms = ['insertion_sort', 'bubble_sort',
                  'merge_sort', 'quick_sort',
                  'builtin_sort']

    # Vælg algoritme (Alle som standard)
    algos = algorithms
    if algo in algorithms:
        # En gyldig algoritme blev valg: Vælg kun den
        algos = [algo]

    # Kør alle algoritmer på listen og mål tid
    results = []
    for algo in algos:
        result = timing.get_time(getattr(sorting, algo), list(lst))
        results.append(result)
    return results
