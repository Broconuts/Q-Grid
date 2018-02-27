#TODO: Laura's code follows a standard that functions start capitalized, Lena's and mine does not. Decide on that.
def ActionSelection(Gridworld, state):
    '''
    Selects the action with the highest q-value for the given state and updates the policy according to the epsilon-soft policy
    :param state: a tuple with the coordinates of the current state
    :return: the action to execute next
    '''


    max = Gridworld.values[state[0]][state[1]]["up"]
    action = "up"

    # find the maximal qvalue in the current state and the according action
    for i in Gridworld.actions:
        if Gridworld.values[state[0]][state[1]][i] > max:
            max = Gridworld.values[state[0]][state[1]][i]
            action = i

    # update the behaviorpolicy with the epsilon-soft formula
    for i in Gridworld.actions:
        if i == action:
            Gridworld.behaviorpolicy[state[0]][state[1]][i] = 1 - Gridworld.epsilon + (Gridworld.epsilon/ len(Gridworld.actions))
        else:
            Gridworld.behaviorpolicy[state[0]][state[1]][i] = Gridworld.epsilon / len(Gridworld.actions)

    return action


def DerivePolicy(Gridworld):
    '''
    make a policy which always chooses the action with the highest q-value
    :return: greedy policy
    '''

    # initialize the policy
    gredpol = [[None for y in range(len(Gridworld.values[0]))] for x in range(len(Gridworld.values))]

    # go over the whole policy
    for i in range(len(Gridworld.values)):
        for j in range(len(Gridworld.values[0])):

            max = Gridworld.values[i][j]["up"]
            action = "up"

            # find the maximal q-value in the state and the according action
            for k in Gridworld.actions:
                if Gridworld.values[i][j][k] > max:
                    max = Gridworld.values[i][j][k]
                    action = k

            # update the state of the policy
            gredpol[i][j] = action

    return gredpol


def qUpdate(Gridworld, state, action, nextstate):
    '''
    Updates the q-value (action-value) for a given state and action.
    :param: Gridworld: the Gridworld we operate in
    :param: state: a tuple with the coordinates of the current state
    :param: action: the action that is used to get to the next state
    :param: nextstate: the state the state-action pair will result in
    '''

    #TODO: check with the others if variable name is okay
    #TODO: also check with others if this somewhat convoluted solution is okay
    # determine the immediate reward for performing a given action in the current state
    # by seeing the immediate reward provided by the next state
    r = immediateReward(Gridworld, nextstate)
    # determine what the highest action-value of the next state is
    nextQmax = max(Gridworld.values[nextstate])

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
    if nature == "E":
        return Gridworld.GOAL
    elif nature == "P":
        return Gridworld.PITFALL
    elif nature == "O":
        #TODO: check with the others if this solution is okay
        return -1000
    elif nature == "F":
        return Gridworld.REWARD


def nextState(Gridworld, state, action):
    '''
    Determines the coordinates of the next state.
    :param: Gridworld: the overall world we act upon
    :param: state: the state currently occupied
    :param: action: the action occuring in that states
    :return: the coordinates of the next state
    '''

    if (action == "up"):
        #TODO: check if state[0] is actually vertical or horizontal line
        # check if we can even move in that direction given our current position
        if (state[0] != 0):
            return (state[0] + 1, state[1])
        #TODO: check with the others if this solution is alright
    elif (action == "down"):
        # check if we can even move in that direction given our current position
        if (state[0] != len(Gridworld.grid) - 1):
            return (state[0] - 1, state[1])
    elif (action == "left"):
        # check if we can even move in that direction given our current position
        if (state[1] != 0):
            return (state[0], state[1] - 1)
    elif (action == "right"):
        # check if we can even move in that direction given our current position
        if (state[1] != len(Gridworld.grid[0]) - 1):
            return (state[0], state[1] + 1)

    else: return state


def updatePolicy(Gridworld):
    '''
    Updates the greedy policy after an episode. Checks for convergence before updating.
    :param Gridworld: the Gridworld we are in
    '''

    newpolicy = DerivePolicy(Gridworld)
    Gridworld.converged = comparePolicies(Gridworld.targetpolicy, newpolicy)
    if not Gridworld.converged:
        Gridworld.targetpolicy = newpolicy


def comparePolicies(policyOne, policyTwo):
    '''
    Checks if two policies are similar.
    :param: policyOne: The first policy to take into consideration.
    :param: policyTwo: The second policy to take into consideration.
    :return: True if policies are the same, False if policies are different
    '''

    for i in range(len(policyOne)):
        for j in range(len(policyOne[0])):
            if policyOne[i][j] != policyTwo[i][j]:
                return False
    return True