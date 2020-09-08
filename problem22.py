# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

import itertools
import basics

def solution1(words, sentence):
    all_combos = []
    solutions = []

    for i in range(1, len(words)+1):
        all_combos += itertools.permutations(words,i)

    for combo in all_combos:
        if ''.join(combo) == sentence:
            solutions.append(combo)

    return solutions

def main():
    wordCount = basics.getNumber()
    words = []
    for i in range(0, wordCount):
        words.append(basics.getString())

    sentence = basics.getString()

    print(solution1(words, sentence))
    

if __name__ == '__main__':
    main()
                
