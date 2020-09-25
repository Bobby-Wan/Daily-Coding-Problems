# This problem was asked by Google.
# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you can 
# walk on.
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number 
# of steps required to reach the end coordinate from the start. If there is no possible 
# path, then return null. You can move up, left, down, and right. You cannot move through 
# walls. You cannot wrap around the edges of the board.
# For example, given the following board:
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of 
# steps required to reach the end is 7, since we would need to go through (1, 2) because 
# there is a wall everywhere else on the second row.

import basics
from collections import deque

class Node:
    def __init__(self, x, y, dist=0):
        self.dist = dist
        self.x = x
        self.y = y

def min_path():
    m = basics.getNumber('Number of columns: ')
    n = basics.getNumber('Number of rows: ')

    matrix = []
    for i in range(0,n):
        row = []    
        for j in range(0,m):
            has_wall = basics.getString()
            if has_wall == 't':
                row.append(True)
            else:
                row.append(False)
        matrix.append(row)

    start_x = basics.getNumber('Start X: ')
    start_y = basics.getNumber('Start Y: ')
    
    end_x = basics.getNumber('End X: ')
    end_y = basics.getNumber('End Y: ')

    visited = []
    for i in range(0,m):
        row = []    
        for j in range(0,n):
            row.append(False)
        visited.append(row)
    
    if (matrix[start_x][start_y] == True):
        return -1
    
    que = deque()
    que.appendleft(Node(start_x, start_y, 0))

    while(len(que) > 0):
        current = que.popleft()
        print('current X: ', current.x, 'current Y: ', current.y, 'dist: ', current.dist)
        if (current.x == end_x and current.y == end_y):
            return current.dist
        print('after condition')
        visited[current.x][current.y] = True

        #Note that normal append() is used here, since we want those nodes pushed
        #to the end
        if(not(current.x + 1 < 0 or current.x + 1 >= m or \
            current.y < 0 or current.y >= n or  \
            visited[current.x+1][current.y] or \
            matrix[current.x+1][current.y])):
            que.append(Node(current.x+1, current.y, current.dist+1))
        if(not(current.x - 1 < 0 or current.x - 1 >= m or \
            current.y < 0 or current.y >= n or \
            visited[current.x-1][current.y] or \
            matrix[current.x-1][current.y])):
            que.append(Node(current.x-1, current.y, current.dist+1))
        if(not(current.x < 0 or current.x >= m or \
            current.y + 1 < 0 or current.y + 1 >= n or \
            visited[current.x][current.y + 1] or \
            matrix[current.x][current.y + 1])):
            que.append(Node(current.x, current.y+1, current.dist+1))
        if(not(current.x < 0 or current.x  >= m or \
            current.y - 1 < 0 or current.y - 1 >= n or \
            visited[current.x][current.y - 1] or \
            matrix[current.x][current.y - 1])):
            que.append(Node(current.x, current.y - 1, current.dist+1))

    return -1

def main():
    print(min_path())

if __name__ == '__main__':
    main()