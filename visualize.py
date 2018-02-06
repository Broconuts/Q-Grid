import math


def printPolicy(Gridworld):
    '''
    Prints policy for each field in the grid correctly formatted in rows and columns
    '''

    print("\n", end="")
    for i in range(len(Gridworld.policy)):
        for j in range(len(Gridworld.policy[0])):
            # prints a symbol representing the direction that the policy for a given field in the grid
            # is indicating
            if (Gridworld.policy[i][j] == "up"):
                print("^", end=" ")
            elif (Gridworld.policy[i][j] == "down"):
                print("v", end=" ")
            elif (Gridworld.policy[i][j] == "left"):
                print("<", end=" ")
            elif (Gridworld.policy[i][j] == "right"):
                print(">", end=" ")
            else:
                print(Gridworld.policy[i][j], end=" ")
        print("\n", end="")


def printValues(Gridworld):
    '''
    Prints value for each field in the grid correctly formatted in rows and columns
    '''
    # iterate over value function
    print("\n", end="")
    for i in range(len(Gridworld.values)):
        for j in range(len(Gridworld.values[0])):
            # checking if nothing (or a placeholder) was written in this position of the array
            if (Gridworld.values[i][j] == "None" or Gridworld.values[i][j] is None):
                print("  x  ", end=" ")
            # printing the value of current position in the array
            # use of ceiling function for rounding up to three decimals is used instead of
            # Python's "round" function since it delivered better results in this program
            else:
                print("{0:5}".format(math.ceil(Gridworld.values[i][j]*1000)/1000), end=" ")
        print("\n", end="")


def printGrid(Gridworld):
    '''
    Prints grid correctly formatted in rows and columns
    :param grid: grid to be printed
    '''

    # for each row aka sublist
    for row in Gridworld.grid:
        # select every element in that sublist (row) and print it
        for elem in row:
            print(elem, end="")  # end="" to substitute the default end of print which is \n by nothing

        print("\n", end="")  # line break after each row
