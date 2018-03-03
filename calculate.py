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
    possibleactions = [0, 1, 2, 3]
    # if chance for following optimal policy is met
    if random.random() < (1- Gridworld.epsilon + Gridworld.epsilon / len(Gridworld.actions)):
        # return action that is currently deemed to be the most valuable one
        return maxaction
    # if chance for optimal policy isn't met, the three remaining options are tried 
    elif random.random() < (Gridworld.epsilon/len(Gridworld.actions)):
        possibleactions.remove(maxaction)
        return possibleactions[0]

    elif random.random() < (Gridworld.epsilon/len(Gridworld.actions)):
        possibleactions.remove(maxaction)
        return possibleactions[1]

    elif random.random() < (Gridworld.epsilon/len(Gridworld.actions)):
        possibleactions.remove(maxaction)
        return possibleactions[2]


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
    r = immediateReward(Gridworld, nextstate)

    # TODO: reformat this formula into something even remotely readable
    q = Gridworld.grid[i][j].value[action] + Gridworld.alpha (r + Gridworld.GAMMA * 
        Gridworld.grid[i][j].max_qValue - Gridworld.grid[i][j].value[action])

    # update the q value for the cell
    Gridworld.grid[i][j].set_qValue(action, q, Gridworld)


def immediateReward(Gridworld, next):
    '''
    Returns the immediate reward for reaching a particular State.
    :param: Gridworld: the Gridworld we operate in
    :param: next: the state we will enter next
    '''

    # TODO: write immediateReward code


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
    (r,c) = state + indact(action)

    valid = validNextState(Gridworld, (r,c))
    if valid:
        return (r,c)
    else:
         return state


def validNextState(Gridworld, state):
    '''
    Returns a boolean that indicates whether the next move leads out of the grid
    :param Gridworld: Grid to operate on
    :param state: current state
    :param action: proposed action
    :return: boolean if action leads out of grid
    '''
    (r,c) = state

    # if the indices are out of the grid it is not a vaild state
    if r < 0 or r >= len(Gridworld.grid):
        return False
    if c < 0 or c >= len(Gridworld.grid[0]):
        return False

    # if there is an obstacle it is not a valid state
    cell = Gridworld.grid[r][c]
    if cell.type == 'O':
        return False

    return True
