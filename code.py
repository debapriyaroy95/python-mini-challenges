# --------------
#Code starts here

import sys

#Function to check for palindrome

#Function to find the smallest palindrome
def palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i

print(palindrome(123))
#palindrome_check(55)            
print(palindrome(1331))     
#Code ends here        


# --------------
# code starts here

from collections import Counter

def a_scramble(str_1,str_2):
    """Test if all the letters of word a are contained in word b"""
    str_1 = str_1.upper()
    str_2 = str_2.upper()
    letters = Counter(str_1)
    letters.subtract(Counter(str_2))
    return all(v >= 0 for v in letters.values())


# --------------
#Code starts here
from math import sqrt

#Code starts here

#Function to check for perfect square 

 
    
#Function to check for fibonacci number
def check_fib(num):
  first = 0
  second = 1
  fibolist = []
  next=0
  for x in range(first,sys.maxsize):
    #next=0
    if next <= num:
      next = first+second
      first=second
      second = next
      fibolist.append(next)
    else:
      break
  result =  num in fibolist
  return result

check_fib(145)   
check_fib(377)   


# --------------
#Code starts here
#Code starts here

#Function to compress string
def compress(word):
    word = word.lower()

    word_copy = ''

    counter = 1

    #Add in first character
    word_copy = word_copy+word[0]

    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            counter=counter+1
        else:
            word_copy = word_copy+str(counter)
            word_copy = word_copy+word[i+1]
            counter = 1
    word_copy = word_copy+str(counter)
    return word_copy

compress("xxcccdex")

    
#Code ends here


# --------------
#Code starts here
def k_distinct(string,k):
  string =string.upper()
  string2 = [x for x in string]
  string2=set(string2)
  result = len(string2)==k
  return result

print(k_distinct('Messoptamia',8))
print(k_distinct('banana',4))


