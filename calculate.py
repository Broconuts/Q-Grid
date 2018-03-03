import random

def selectAction(Gridworld, state):
    '''
    Selects the action with the highest q-value for the given state and updates the policy according to the epsilon-soft policy
    :param state: a tuple with the coordinates of the current state
    :return: the action to execute next
    '''

    maxaction = Gridworld.grid[state].max
    # TODO: can we also use Gridworld.actions for this or is it mutable (i.e. would removing the max value for this function remove 
    # an actual entry from the original array)?
    possibleActions = [0, 1, 2, 3]
    # if chance for following optimal policy is met
    if random.random() < (1- Gridworld.epsilon + Gridworld.epsilon / len(Gridworld.actions)):
        # return action that is currently deemed to be the most valuable one
        return maxaction
    # if chance for optimal policy isn't met, on of the others returned randomly
    else:
        possibleActions.remove(maxaction)
        return random.choice(possibleActions)



def qUpdate(Gridworld, state, action, nextstate):
    '''
    Updates the q-value (action-value) for a given state and action.
    :param: Gridworld: the Gridworld we operate in
    :param: state: a tuple with the coordinates of the current state
    :param: action: the action that is used to get to the next state
    :param: nextstate: the state the state-action pair will result in
    '''

    # determine the immediate reward for performing a given action in the current state
    # by seeing the immediate reward provided by the next state
    im_reward = immediateReward(Gridworld, nextstate)

    # assigments for easier access
    row = state[0]
    column = state[1]
    cell = Gridworld.grid[row][column]
    old_qVal = cell._qValues[action]

    #q(s,a) + alpha * (reward + gamma * max q(s,a) - q(s,a) )
    new_qVal = old_qVal + Gridworld.alpha * \
               (im_reward + Gridworld.GAMMA * cell._max - old_qVal)

    # update the q value for the cell
    cell.set_qValue(action, new_qVal, Gridworld)


def immediateReward(Gridworld, next):
    '''
    Returns the immediate reward for reaching a particular State.
    :param: Gridworld: the Gridworld we operate in
    :param: next: the state we will enter next
    '''

    #get cell representation
    cell = Gridworld.grid[next[0]][next[1]]

    #check what type cell is and return corresponding value
    if cell._type == "F":
        return Gridworld.REWARD
    elif cell._type == "E":
        return Gridworld.GOAL
    elif cell._type == "O":
        return -1000
    elif cell._type == "P":
        return Gridworld.PITFALL
    else:
        print("Field Type not found! Problem in immediateReward")
        exit(1)


def nextState(Gridworld, state, action):
    '''
    Determines the coordinates of the next state.
    :param: Gridworld: the overall world we act upon
    :param: state: the state currently occupied
    :param: action: the action occuring in that states
    :return: the coordinates of the next state
    '''
    # get the indexshift for the according action
    def indact(ind):
        return {
            0: (1,0),
            1: (-1,0),
            2: (0,-1),
            3: (0,1),
        }[ind]

    # the indices of the new state

    (row,column) = (state[0] + indact(action)[0], state[1] + indact(action)[1])

    valid = validNextState(Gridworld, (row,column))
    if valid:
        return (row,column)
    else:
         return state


def validNextState(Gridworld, nextstate):
    '''
    Returns a boolean that indicates whether the next move leads out of the grid
    :param Gridworld: Grid to operate on
    :param nextstate: state to be checked
    :param action: proposed action
    :return: boolean if action leads out of grid
    '''
    (row,column) = nextstate

    # if the indices are out of the grid it is not a vaild state
    if row < 0 or row >= len(Gridworld.grid):
        return False
    if column < 0 or column >= len(Gridworld.grid[0]):
        return False

    # if there is an obstacle it is not a valid state
    cell = Gridworld.grid[row][column]
    if cell.type == 'O':
        return False

    return True
