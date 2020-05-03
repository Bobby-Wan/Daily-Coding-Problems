def getNumberList():
    line = input('Input comma separated list: ')
    line_split = line.split()
    integers = []
    for word in line_split:
        integers.append(int(word))
    return integers

def getNumber():
    number = input('Input number: ')
    return int(number)
