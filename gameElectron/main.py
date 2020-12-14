# https://www.codewars.com/kata/52210226578afb73bd0000f1/train/python

def electrons_around_the_cores(dice):
    # Just so you can try some numbers
    ans = 0
    for number in dice:
        if number%2!=0:
            ans = ans +number
    
    ans = ans -1 

    return ans