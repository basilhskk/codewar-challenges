def solution(nums):
    arr = []

    for number in range(nums):
        print(number)
        if number%5 == 0 or number%3 == 0:
            arr.append(number)
    ans = sum(arr)
    print(ans)

    return ans

solution(10)