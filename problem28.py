# This problem was asked by Palantir.
# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify(text, k):
    if not text:
        return None

    words = text.split()
    lines = list()
    line = list()
    line.append(words[0])
    current_length = len(words[0])
    
    for i in range(1,len(words)):
        if(current_length + len(words[i]) + 1 <= k):
            current_length += len(words[i]) + 1
            line.append(words[i])
        else:
            lines.append(line)
            line = list()
            line.append(words[i])
            current_length = len(words[i])

    lines.append(line)
    
    for l in lines:
        word_count = len(l)
        total_length = 0
        for e in l:
            total_length += len(e)
        empty = k-total_length
        spaces = word_count-1
        empty_symbols_per_space = empty//spaces
        leftover = empty%spaces

        to_print = ''
        for (i,e) in enumerate(l):
            to_print += e
            for _ in range(empty_symbols_per_space):
                to_print += ' '
            if i/2 + 1 <= leftover:
                to_print += ' '
        
        print(to_print)

def main():
    justify('the quick brown fox jumps over the lazy dog', 16)

if __name__ == '__main__':
    main()