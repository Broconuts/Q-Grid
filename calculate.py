import random

def selectAction(Gridworld, state):
    '''
    Selects the action with the highest q-value for the given state and updates the policy according to the epsilon-soft policy
    :param state: a tuple with the coordinates of the current state
    :return: the action to execute next
    '''

    rand = random.random()
    maxaction = Gridworld.grid[state].max
    # TODO: can we also use Gridworld.actions for this or is it mutable (i.e. would removing the max value for this function remove 
    # an actual entry from the original array)?
    possibleactions = [0, 1, 2, 3]
    # if chance for following optimal policy is met
    if rand < (1- Gridworld.epsilon + Gridworld.epsilon / len(Gridworld.actions):
        # return action that is currently deemed to be the most valuable one
        return maxaction
    # TODO: if we implement the formula from the slides, we only get a total probability of 0.8 to do an action
    # not sure if that is correct and that there is a .2 chance of not doing anything?
    elif rand < (Gridworld.epsilon/len(Gridworld.actions)):
        max.remove(maxaction)
        return random.choice(possibleactions)


def derivePolicy(Gridworld):
    '''
    make a policy which always chooses the action with the highest q-value
    :return: greedy policy
    '''

    #TODO: write the code for derivePolicy


def qUpdate(Gridworld, state, action, nextstate):
    '''
    Updates the q-value (action-value) for a given state and action.
    :param: Gridworld: the Gridworld we operate in
    :param: state: a tuple with the coordinates of the current state
    :param: action: the action that is used to get to the next state
    :param: nextstate: the state the state-action pair will result in
    '''

    # TODO: write qUpdate code


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

    #TODO: write the code for nextState


def updatePolicy(Gridworld):
    '''
    Updates the greedy policy after an episode. Checks for convergence before updating.
    :param Gridworld: the Gridworld we are in
    '''

    # TODO: write updatePolicy code


def comparePolicies(policyOne, policyTwo):
    '''
    Checks if two policies are similar.
    :param: policyOne: The first policy to take into consideration.
    :param: policyTwo: The second policy to take into consideration.
    :return: True if policies are the same, False if policies are different
    '''

    # TODO: write comparePolicies code


def validNextState(Gridworld, state, action):
    '''
    Returns a boolean that determines whether the next move leads out of the grid
    :param Gridworld: Grid to operate on
    :param state: current state
    :param action: proposed action
    :return: boolean if action leads out of grid
    '''
    # TODO: write validNextState code
