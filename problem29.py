# This problem was asked by Amazon.
# Run-length encoding is a fast and simple 
# method of encoding strings. The basic idea is
# to represent repeated successive characters as
# a single count and character. For example, 
# the string "AAAABBBCCDAA" would be encoded 
# as "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def encode(string):
    count=1
    result = ''
    for i in range(len(string)):
        if i == len(string) - 1:
            result += str(count) + string[i]
        elif string[i] != string[i+1]:
            result += str(count) + string[i]
            count = 1
        else:
            count += 1

    return result

def is_digit(c):
    return c>='0' and c<='9'

def decode(string):
    count = ''
    result = ''
    for i in range(len(string)):
        if(is_digit(string[i])):
            count += string[i]
        else:
            for _ in range(int(count)):
                result += string[i]
            count = ''
    
    return result


def main():
    print(decode(encode('AAAABBBCCDAA')))

if __name__ == '__main__':
    main()