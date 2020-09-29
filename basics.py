import requests

def getNumberList(text = None):
    if(text == None):
        line = input('Input space separated list: ')
    else:
        line = text

    line_split = line.split()
    integers = []
    for word in line_split:
        integers.append(int(word))
    
    return integers

def getNumber(message=''):
    number = input(message)
    return int(number)

def getIntegerListFromAPI(size, min, max):
    apiUrl = 'https://www.random.org/integers/?num=' + str(size) + \
        '&min=' + str(min) + '&max=' + str(max) + '&col=' + str(size) + '&base=10&format=plain&rnd=new'

    response = requests.get(url = apiUrl)
    if response.status_code == 200:
        data = response.content
        decoded_data = data.decode('UTF-8')
        return getNumberList(decoded_data)
    raise NameError('Bad request.')

def rotateListRight(list, index):
    length = len(list)
    if length == 0 or length == 1:
        return list
    if index == 0:
        return list

    rotated = []
    if index > length:
        index = index % length

    print('Index: ', index)
    print('Length: ', length)

    for i in range(length-index,length):
        rotated.append(list[i])
    for i in range(0,length-index):
        rotated.append(list[i])

    return rotated

def getString():
    return input('Input string: ')
