# This problem was asked by Facebook.
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def are_symmetrical(left, right):
    return (left == '(' and right == ')') or \
        left == '[' and right == ']' or \
        left == '{' and right == '}'

def is_brace(c):
    return c in ['(',')','{','}','[',']']

def is_balanced(string):
    stack = list()
    for char in string:
        if stack and is_brace(char) and are_symmetrical(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)

    return not stack


def main():
    assert is_balanced('[][]')
    assert is_balanced('([])[]({{}})')
    print('Hooray!')
    
if __name__ == '__main__':
    main()