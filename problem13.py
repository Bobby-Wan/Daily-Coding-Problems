# Good morning! Here's your coding interview problem 
# for today.
# This problem was asked by Amazon.
# Given an integer k and a string s, 
# find the length of the longest substring that 
# contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, 
# the longest substring with k distinct characters 
# is "bcb"

def longest_substring(s, k):
    length = len(s)
    longest_string = ''
    max_length = 0

    if distinct_characters(s) == k and len(s) > max_length:
                longest_string = s
                max_length = length

    for i in range(length):
        for j in range(length-1, i, -1):
            
            if distinct_characters(s[i:j]) == k and len(s[i:j]) > max_length:
                longest_string = s[i:j]
                max_length = len(longest_string)
    
    return longest_string

def distinct_characters(str):
    length = len(str)
    distinct_chars = []
    for i in range(length):
        if not distinct_chars.__contains__(str[i]):
            distinct_chars.append(str[i])
    
    return len(distinct_chars)


def main():
    print(longest_substring('abcba',2))

if __name__ == '__main__':
    main()
