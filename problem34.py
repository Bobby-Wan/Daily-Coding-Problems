# This problem was asked by Quora.
# Given a string, find the palindrome that can be made by 
# inserting the fewest number of characters as possible anywhere 
# in the word. If there is more than one palindrome of minimum 
# length that can be made, return the lexicographically earliest 
# one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", 
# since we can add three letters to it (which is the smallest 
# amount to make a palindrome). There are seven other palindromes 
# that can be made from "race" by adding three letters, 
# but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should 
# return "elgoogle".

def is_palidrome(s):
    return s[::-1] == s

def make_palindrome(word):
    if is_palidrome(word):
        return word
    
    if word[0] == word[-1]:
        return word[0] + make_palindrome(word[1:-1]) + word[-1]
    else:
        pal1 = word[0] + make_palindrome(word[1:]) + word[0]
        pal2 = word[-1] + make_palidrome(word[:-1]) + word[-1]

        if len(pal1) < len(pal2):
            return pal1
        if len(pal1) > len(pal2):
            return pal2

        return pal1 if pal1<pal2 else pal2

    
    
    
if __name__ == "__main__":
    assert is_palidrome('ecarace')
    assert is_palidrome('elgoogle')
    assert is_palidrome('abcdcba')
    assert is_palidrome('')
    
    assert make_palindrome('race') == 'ecarace'
    assert make_palindrome('ecar') == 'ecarace'
    assert make_palindrome('google') == 'elgoogle'
    assert make_palindrome('elgoog') == 'elgoogle'
    assert make_palindrome('abcd') == 'abcdcba'
    assert make_palindrome('dcba') == 'abcdcba'



    