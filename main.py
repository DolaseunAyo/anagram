# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    return True
    
string1 = input('Enter first word \n')
string2 = input('Enter second word \n')

if(sorted(string1) == sorted(string2)):
    print("True")
else:
    print('False')

