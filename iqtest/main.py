# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(numbers):
    #your code here
    nums = numbers.split(" ")

    data1nums = []
    data2nums = []
    ans = ""

    for i,num in enumerate(nums):
        num = int(num)
        if num%2==0:
            data1nums.append(i)
        else:
            data2nums.append(i)

    

    if len(data1nums)<len(data2nums):
        ans = data1nums[0] +1
    else:
        ans = data2nums[0] +1

    return ans






print(iq_test("2 4 7 8 10"))