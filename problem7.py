# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
    
def decoding_ways(str):
    if len(str) == 0:
        return 1
    if len(str) == 1:
        return 1
    length=len(str)
    if length >= 2:
        if int(str[0:2]) > 26: 
            return decoding_ways(str[1:])
        else:
            if str[1] == '0':
                return decoding_ways(str[2:])
            return decoding_ways(str[1:]) + decoding_ways(str[2:])

def main():
    string = '111'
    print(decoding_ways(string))

if __name__ =='__main__':
    main()