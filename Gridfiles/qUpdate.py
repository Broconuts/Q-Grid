def qUpdate(Gridworld, state, action):
    '''
    Updates the q-value (action-value) for a given state and action.
    :param: Gridworld: the Gridworld we operate in
    :param: state: a tuple with the coordinates of the current state
    :param: action: the action that is used to get to the next state
    '''

    #TODO: check with the others if variable name is okay
    #TODO: also check with others if this somewhat convoluted solution is okay
    # determine what the next state is for a given state and a given action
    ns = nextState (state, action)
    # determine the immediate reward for performing a given action in the current state
    # by seeing the immediate reward provided by the next state
    r = immediateReward(Gridworld, nextState)
    # determine what the highest action-value of the next state is
    nextQmax = max(Gridworld.values[ns])

    # calculate action-value of the current action given the current state
    # result of the immediate reward plus the best action-value of the next states
    # remember: Gridworld.alpha is the learning rate of our learner
    Gridworld.values[state][action] = r + Gridworld.alpha * nextQmax


def immediateReward(Gridworld, next):
    '''
    Returns the immediate reward for reaching a particular State.
    :param: Gridworld: the Gridworld we operate in
    :param: next: the state we will enter next
    '''

    # retrieve the string representing the nature of the field we are about to enter
    nature = Gridworld.grid[next[0]][next[1]]

    # return according reward
    if nature = "E":
        return Gridworld.GOAL
    elif nature = "P":
        return Gridworld.PITFALL
    elif nature = "O"
        #TODO: check with the others if this solution is okay
        return -1000
    elif nature = "F":
        return Gridworld.REWARD


def nextState(state, action):
    '''
    Determines the coordinates of the next state.
    :param: Gridworld: the overall world we act upon
    :param: state: the state currently occupied
    :param: action: the action occuring in that states
    :return: the coordinates of the next state
    '''

    if (action = "up"):
        #TODO: check if state[0] is actually vertical or horizontal line
        # check if we can even move in that direction given our current position
        if (state[0] != 0):
            return (state[0] + 1, state[1])
        #TODO: check with the others if this solution is alright
    elif (action = "down"):
        # check if we can even move in that direction given our current position
        if (state[0] != len(Gridworld.grid) - 1):
            return (state[0] - 1, state[1])
    elif (action = "left"):
        # check if we can even move in that direction given our current position
        if (state[1] != 0):
            return (state[0], state[1] - 1)
    elif (action = "right"):
        # check if we can even move in that direction given our current position
        if (state[1] != len(Gridworld.grid[0]) - 1):
            return (state[0], state[1] + 1)

    else return state
