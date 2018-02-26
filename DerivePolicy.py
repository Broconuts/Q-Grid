def DerivePolicy():
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
