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
