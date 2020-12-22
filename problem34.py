def is_palidrome(s):
    return s[::-1] == s

def make_palindrome(word):
    if is_palidrome(word):
        return word
    
    if word[0] == word[-1]:
        return word[0] + make_palindrome(word[1:-1]) + word[-1]
    else:
        pal1 = word[0] + make_palindrome(word[1:]) + word[0]
        pal2 = word[-1] + make_palindrome(word[:-1]) + word[-1]

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



    