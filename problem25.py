# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and 
# returns whether or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should
# return true. The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return 
# true. The same regular expression on the string "chats" should return false.

def matches(regex, string):
    if not regex:
        return not string

    first_letter_matches = bool(string) and regex[0] in (string[0], '.')

    if len(regex) >= 2 and regex[1] == '*':
        return matches(regex[2:], string) or \
            (first_letter_matches and matches(regex,string[1:]))
    else:
        return first_letter_matches and matches(regex[1:],string[1:])

def main():
    assert matches("ra.", "ray")
    assert not matches("ra.", "raymond")
    assert matches(".*at", "chat")
    assert not matches(".*at", "chats")
    assert matches(".*at", 'chaat')

if __name__ == '__main__':
    main()