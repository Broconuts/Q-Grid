from itertools import chain, zip_longest
import Gridworld
import sys


def printPolicy(Gridworld):
    '''
    Prints policy for each field in the grid correctly formatted in rows and columns
    '''

    print("\n", end="")
    for i in range(len(Gridworld.grid)):
        for j in range(len(Gridworld.grid[0])):
            cell = Gridworld.grid[i][j]
            # prints a symbol representing the direction that the policy for a given field in the grid
            # is indicating
            if (cell._max == 0):
                print("^", end=" ")
            elif (cell._max == 1):
                print("v", end=" ")
            elif (cell._max == 2):
                print("<", end=" ")
            elif (cell._max == 3):
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
    print("Key:")
    print("(up, down)")
    print("(left, right)")
    print("\n")

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


def readUserInput(Gridworld):
    '''
    Reads in user input:
    - gridfile = grid to perform q-learning on
    - processing mode = one of three possibilities
        - manual: stepwise for each episode, matrix for each step
        - semi-automatic: each episode automatic, matrices printed after that
        - automatic: complete algorithm, matrices printed once in the end
    - gamma value = discount factor
    - epsilon = for epsilon soft policy
    - alpha = learning rate
    - reward = penalty for each step
    - goal = reward at the goal state
    - pitfall = penalty in the trap state
    '''

    # read in grid file
    inputPath = input("Please specify a valid grid file (no need for the \".grid\"-ending): ")
    pathToGrid = inputPath.lower() + ".grid"

    grid = []  # empty list as grid

    try:
        # open file
        with open(pathToGrid, "r") as f:
            line = f.readline()  # read first line

            # while line not empty (still new line to read)
            while line:
                stripped_line = line.strip("\n")  # remove line break
                splitted_line = stripped_line.split(" ")  # split line at whitespace to get elements
                grid.append(splitted_line)  # append to grid to make list of lists
                line = f.readline()  # read next line

    except IOError:  # catch IO error from opening file
        print("Gridfile could not be found: Please specify a valid file (no need for the .grid-ending).")
        exit(1)

    # read in processing mode from user (a or m or s)
    processingMode = input("Please choose between manual, semi-automated and automated processing (a/s/m): ")
    while not (processingMode.lower() == "a" or processingMode.lower() == "m" or processingMode.lower() == "s"):
        processingMode = input("Please choose between manual, semi-automated and automated processing (a/s/m): ")

    # read in gamma as float
    gamma = float(input("Please specify a discount factor gamma value between 0 and 1: "))
    while gamma > 1.0 or gamma < 0.0:
        gamma = float(input("Please specify a gamma value between 0 and 1: "))

    # read in epsilon value as float
    epsilon = float(input("Please specify an epsilon for the epsilon-soft-policy between 0 and 1: "))
    while epsilon > 1.0 or epsilon < 0.0:
        epsilon = float(input("Please specify an epsilon for the epsilon-soft-policy value between 0 and 1: "))

    # read in learning rate
    alpha = float(input("Please specify a learning rate alpha between 0 and 1: "))
    while alpha > 1.0 or alpha < 0.0:
        alpha = float(input("Please specify a learning rate alpha value between 0 and 1: "))

    # read in convergence criterion
    convergencecriterion = int(input("Please specify how many iterations in a row the policy should stay the same for convergence: "))
    while convergencecriterion <= 0:
        convergencecriterion = int(input("Please specify how many iterations in a row the policy should stay the same for convergence: "))

    # assign the values to the Gridworld
    Gridworld.field = grid #not grid since it will be converted into cells
    Gridworld.processingMode = processingMode.lower()
    Gridworld.gamma = gamma
    Gridworld.alpha = alpha
    Gridworld.epsilon = epsilon
    Gridworld.convergencecriterion = convergencecriterion

    # check for correctness of input
    # since it is absolutely up to the user which values these variables take
    # we only check for input type
    try:
        Gridworld.REWARD = input("Please specify the reward (or penalty) for each step: ")
        if ("exit" in Gridworld.REWARD.lower()):
            sys.exit()
        Gridworld.REWARD = float(Gridworld.REWARD)
        
        Gridworld.GOAL = input("Please specify the reward of the goal state: ")
        if ("exit" in Gridworld.GOAL.lower()):
            sys.exit()
        Gridworld.GOAL = float(Gridworld.GOAL)
        
        Gridworld.PITFALL = input("Please specify the penalty for the pitfall state: ")
        if ("exit" in Gridworld.PITFALL.lower()):
            sys.exit()
        Gridworld.PITFALL = float(Gridworld.PITFALL)
    
    except ValueError:
        print("Stop this tomfoolery and enter a float value between 0 and 1! Try again next time.")
        sys.exit()

