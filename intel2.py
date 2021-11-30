import sys

prueba1 = "A dog, a plan, a canal: pagoda"


def palindromes(s):
    eq =  True
    s = s.lower()
    s = list(s)
    for letter in s:
        if letter > "z" or letter < "a":
            del letter
    print(s)
    n = len(s)//2
    for i in range(n):
        eq *= (s[i]==s[-i-1])
    return eq



print(palindromes(prueba1))