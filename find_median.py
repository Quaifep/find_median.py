# Author: Paul Quaife
# Date: 2/12/2021
# Description: Takes a list of numbers. The function should return the statistical median of those numbers.

def find_median(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[len(lst)//2]
    else:
        return (lst[len(lst) // 2-1] + lst[len(lst) // 2])/2
    