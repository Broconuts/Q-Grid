import math


#TODO convert this function so that it works in its exported form
def read(Gridworld):
    '''
    Reads a grid file from command line arguments

    :return: grid as list of lists
    each sublist is a row
    e.g. grid[0][1] accesses the second element in the first sublist aka the second element in row 0
    grid[0][1] corresponds to (1,0) in "point notation" (x,y)
    '''

    file = ""
    try:
        # access command line arguments, if not empty string
        # (sys.argv[0] is program file, sys.argv[1] ist first argument)
        if sys.argv[1]:
            file += sys.argv[1]
    except IndexError:  # sys.argv[1] unspecified means that no further argument is given
        print("Please specify a grid file")
        exit(1)  # stop execution of program

    grid = []  # empty list as grid

    try:
        # open file
        with open(file, "r") as f:
            line = f.readline()  # read first line

            # while line not empty (still new line to read)
            while line:
                stripped_line = line.strip("\n")  # remove line break
                splitted_line = stripped_line.split(" ")  # split line at whitespace to get elements
                grid.append(splitted_line)  # append to grid to make list of lists
                line = f.readline()  # read next line

    except IOError:  # catch IO error from opening file
        print("Gridfile could not be found: Please specify a valid file (with path).")
        exit(1)

    self.grid = grid


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
