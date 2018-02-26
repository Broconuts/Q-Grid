def ActionSelection(state):
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
