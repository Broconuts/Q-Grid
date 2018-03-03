from itertools import chain, zip_longest
import Gridworld

def printQValues(Gridworld):
    '''
    Prints values of action to change from one state to another.
    '''

    #TODO: write the code for printQValues


def printPolicy(Gridworld):
    '''
    Prints policy for each field in the grid correctly formatted in rows and columns
    '''

    print("\n", end="")
    for i in range(len(Gridworld.grid)):
        for j in range(len(Gridworld.grid[0])):
            # prints a symbol representing the direction that the policy for a given field in the grid
            # is indicating
            if (Gridworld.grid[i][j].policy == 0):
                print("^", end=" ")
            elif (Gridworld.grid[i][j].policy == 2):
                print("v", end=" ")
            elif (Gridworld.grid[i][j].policy == 1):
                print("<", end=" ")
            elif (Gridworld.grid[i][j].policy == 3):
                print(">", end=" ")
            else:
                print("o", end=" ")
        print("\n", end="")


def continuationRequest():
    '''
    Checks if user wants to continue calculating episodes.
    :return: Returns True if user wants to continue, returns False if user does not
    '''

    choice = input("Episode has concluded. Do you want to continue? (y/n) ")
    while not (choice is "y" or "n" or "Y" or "N"):
        if "exit" in choice.lower():
            sys.exit()
        choice = input("Please select either yes (y) or no (n): ")

    if choice.lower() == "y":
        return True

    return False

def printQValues(Gridworld):
    '''
    Prints values of action to change from one state to another.
    '''

    # creates an array of strings from the print strings from all cells
    table = []
    for r in range(len(Gridworld.grid)):
        row = []
        for c in range(len(Gridworld.grid[0])):
            pristri = Gridworld.grid[r][c].get_print_string()
            row.append(pristri)
        table.append(row)

    # adds everything together to reformat
    matrix = chain.from_iterable(
        zip_longest(
            *(x.splitlines() for x in y),
            fillvalue='')
        for y in table)

    # nice formatting
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]

    # for better visibility add an empty line in every second place
    # meaning after every row of the grid
    counter = 0
    for ind in table:
        if counter % 2 != 0:
            table[counter] = table[counter] + "\n"
        counter = counter + 1

    # print all array values from table each in a new line
    print('\n'.join(table))
