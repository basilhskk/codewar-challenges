# Range Extraction 
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

from itertools import groupby
def group_consecutives(lst):
    for _, g in groupby(enumerate(lst), lambda i_x : i_x[0] - i_x[1]):
        r = [x for _, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)

def solution(numbers):
    return ','.join(group_consecutives(numbers))


a = solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) # '-6,-3-1,3-5,7-11,14,15,17-20'
print(a)
solution([-3,-2,-1,2,10,15,16,18,19,20]) #, '-3--1,2,10,15,16,18-20'