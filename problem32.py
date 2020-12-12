currencies = ['BGN','USD','EURO','AUD']

exchange_rates = [[1, 1.7, 1.9, 2],\
                [1, 0.58, 0.52, 0.5],\
                [1,2,3,4],\
                [4,5,6,7]]

#A couple of ways to interpret this task, will choose
#the easier one to implement ofcourse.
def get_arbitrage(rates):
    # a - a -> 1
    # a - b -> x
    # b - a -> 1/x

    for i in range(len(rates)):
        for j in range(i, len(rates)):
            if rates[i][j] * rates[j][i] > 1:
                return True

    
    return False

if __name__ == '__main__':
    
