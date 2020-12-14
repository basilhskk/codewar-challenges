# First non-repeating character
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
    string = string.strip()
    for letter in string:

        islower = letter.islower()
        string = string.lower()
        data = string.split(letter.lower())
        
        if len(data) <= 2:
            if islower:
                return letter
            else:
                return letter.upper()
    
    return ""




a =first_non_repeating_letter('hello world, eh?')
print ( a )
a = first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')
print ( a )
a = first_non_repeating_letter('sTreSS')
print ( a )

