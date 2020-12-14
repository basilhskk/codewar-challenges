# Real Password Cracker
# https://www.codewars.com/kata/59146f7b4670ba520900000a/train/python
import hashlib 
from itertools import product
import itertools
from string import ascii_lowercase

def password_cracker(hash):
    ans = ""

    for length in range(6):
        for candidate in map("".join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length)):
            if hashlib.sha1(candidate.encode()).hexdigest() == hash:
                return candidate


password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e')#, 'code'

password_cracker('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3')#, 'test'