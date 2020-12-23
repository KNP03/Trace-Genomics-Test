# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:10:19 2020
Garden test : Takes in a Matrix as input and provides a whole number as output based on the calulations below. 
"""

def find_center(matrix):
    '''
    Return an x,y coord thats either the dead center of the matrix,
    If there are more than one center, return the largest of all the center cells.
    '''
    #Part-1 : find x,y coord
    # find the middle y coord.
    if len(matrix) % 2 == 1: #For the given test case len=4 hence 4 % 2 == 0, hence it will jump to else
        middlex = int(len(matrix) / 2)
    else:
        middlex = (int(len(matrix) / 2 - 1), int(len(matrix) / 2)) # Ans : (1.0,2.0)
    # and the x coord
    if len(matrix[0]) % 2 == 1: #yes , middley= 2.5
        middley = int(len(matrix[0]) / 2)
    else:
        middley = (int(len(matrix[0]) / 2 - 1), int(len(matrix[0]) / 2))

    # both inner and outer arrays are odd,  there's a dead center.
    if type(middlex) == int and type(middley) == int: 
        return (middlex, middley)
    # inner array is even - In this case, middlex is a tuple and middley is an int, so this is the loop it chooses
    if type(middlex) == tuple and type(middley) == int: 
        middle_cell = [(middlex[0], middley), (middlex[1], middley)] # middle_cell =[(1, 2), (2, 2)] 
    # outer array is even
    elif type(middlex) == int and type(middley) == tuple:
        middle_cell = [(middlex, middley[0]), (middlex, middley[1])]
    #  if neither has a middle,  get all four center cells
    if type(middley) == tuple and type(middlex) == tuple:
        middle_cell = [(middlex[0], middley[0]), (middlex[1], middley[0]), 
                        (middlex[0], middley[1]), (middlex[1], middley[1])]
    
    #Part-2 : find the largest cell
    largest_value = -1
    # find the largest cell of the middle
    for cell in middle_cell:
        #only takes in int values since list indices must be integers not tuples or float values
        #Hence values inside tuples are converted to int in the previous loop
        if matrix[cell[0]][cell[1]] > largest_value: 
            largest_value = matrix[cell[0]][cell[1]]
            largest_cell = cell #(1,2)
    return largest_cell


def get_largest_adjacent(cell, matrix):
    '''
    return the largest adjascent cell.
    if there are no cells with carrots,  return None
    '''

    x, y = cell
    adj = [] #create an emplty list 
    #  Collect all cells to the right, left, above, and below current cell.
    if x != 0:
        adj.append((x - 1, y)) #append to the empty list
    if y != 0:
        adj.append((x, y - 1))
    if x != len(matrix) - 1:
        adj.append((x + 1, y))
    if y != len(matrix) - 1:
        adj.append((x, y + 1))

    # return the cell with the most carrots.  if all cells are empty,  return None 
    # meaning the rabbit sleeps without eating carrots
    largest = 0
    largest_cell = None
    for a_cell in adj:
        if matrix[a_cell[0]][a_cell[1]] > largest:
            largest = matrix[a_cell[0]][a_cell[1]]
            largest_cell = a_cell
    return largest_cell


def eat(matrix):
    '''
    
    calcluates carrots eaten based on the matrix given below.

    '''
    x, y = find_center(matrix)
    carrots_eaten = matrix[x][y]
    adj = get_largest_adjacent((x, y), matrix)
    while adj is not None:
        carrots_eaten += matrix[adj[0]][adj[1]]
        matrix[adj[0]][adj[1]] = 0
        adj = get_largest_adjacent(adj, matrix)
    return carrots_eaten



# Test case
garden1 = [
    [5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8]]

if __name__ == '__main__': #run the eat(matrix) function on the test
    test = eat(garden1)
    print ('The number of carrots Bunny eats before falling asleep is {}'.format(test)) #ouput for this is 27

