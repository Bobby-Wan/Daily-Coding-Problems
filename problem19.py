# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

import basics

def cheapestCombination(prices):
    number_of_houses = len(prices)
    if(number_of_houses == 0):
        print('Incorrect input..')
        return

    number_of_colors = len(prices[0])
    if(number_of_colors == 0):
        print('Incorrect input..')
        return

    #Initialize total cost matrix with 0s
    total_cost_matrix = []
    for i in range(number_of_houses):
        colors = []
        for j in range(number_of_colors):
            colors.append(0)
        total_cost_matrix.append(colors)
    

    for i in range(number_of_houses):
        if(i == 0):
            for j in range(number_of_colors):
                total_cost_matrix[i][j] = prices[i][j]
        else:
            for j in range(number_of_colors):
                previous_values = list(total_cost_matrix[i-1])
                print('previous values: ', previous_values)
                previous_values.pop(j)
                min_value = min(previous_values)
                print('min prev value: ', min_value)

                total_cost_matrix[i][j] = prices[i][j] + \
                    min_value
                print('price: ',total_cost_matrix[i][j])
    
    print(total_cost_matrix)

def main():
    print('Number of houses: ')
    number_of_houses = basics.getNumber()
    print('Number of colors: ')
    number_of_colors = basics.getNumber()

    prices=[]
    for h in range(number_of_houses):
        print('House ',h,' prices: ')
        colors = basics.getNumberList()
        if(len(colors) != number_of_colors):
            print('Input length not matching number of colors..')
            return
        
        prices.append(colors)

    print(prices)
    cheapestCombination(prices)


if __name__ == '__main__':
    main()