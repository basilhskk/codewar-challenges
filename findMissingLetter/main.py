# Find the missing letter
# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python

def find_missing_letter(chars):
    ans = ""

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    islower = chars[0].islower()
    chars = [x.lower() for x in chars]
    
    start = alphabet.index(chars[0])
    end = alphabet.index(chars[-1])

    complete = alphabet[start:end+1]

    missing = list(set(complete)-set(chars))

    if islower:
        ans = missing[0]
    else:
        ans = missing[0].upper()
    print(ans)
    return ans


find_missing_letter(['A','B','C','D','F'])