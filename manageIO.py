import math
import sys

def continuationRequest():
    '''
    Checks if user wants to continue calculating episodes.
    :return: Returns True if user wants to continue, returns False if user does not
    '''

    choice = input("Episode has concluded. Do you want to continue? (y/n)")
    while not (choice is "y" or "n" or "Y" or "N"):
        if "exit" in choice.lower():
            sys.exit()
        choice = input("Please select either yes (y) or no (n): ")

    if choice.lower() is "y":
        return True

    return False


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
                print("{0:5}".format(math.ceil(Gridworld.values[i][j] * 1000) / 1000), end=" ")
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

    # read in processing mode from user (a or m)
    processingMode = input("Please choose between manual, semi-automated and automated processing (a/s/m): ")
    while not (processingMode.lower() == "a" or processingMode.lower() == "m" or processingMode.lower() == "s"):
        processingMode = input("Please choose between manual, semi-automated and automated processing (a/s/m): ")

    # read in gamma as float
    gamma = float(input("Please specify a gamma value between 0 and 1: "))
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

    # assign the values to the Gridworld
    Gridworld.grid = grid
    Gridworld.processingMode = processingMode.lower()
    Gridworld.gamma = gamma
    Gridworld.alpha = alpha
    Gridworld.epsilon = epsilon

    # @TODO maybe implement goal > pitfall?
    Gridworld.REWARD = float(input("Please specify the reward (or penalty) for each step: "))
    Gridworld.GOAL = float(input("Please specify the reward of the goal state: "))
    Gridworld.PITFALL = float(input("Please specify the penalty for the pitfall state: "))
