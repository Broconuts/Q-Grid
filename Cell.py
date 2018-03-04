import numpy as np

class Cell:
    '''
    Conceptualizes a cell of Gridworld with the required properties of such a type.
    A cell has a type (either free, obstacle, pitfall or exit), a policy (greedy action), 
    a value for each action, and the index of the highest value (for ease of access).
    '''

    def __init__(self, actions, type):
        self._type = type
        self._policy = 0
        self._max = 0 # idx of maximal qValue
        # free fiels get q-value array
        if self._type == "F":
            self._qValues = np.zeros(actions)
            self._qValues = [0 for x in range(actions)]
        # other fields get their type as array and max-index of -1
        else:
            self._qValues = [type, type, type, type]
            self._max = -1


    @property
    def policy(self):
        '''
        The action policy for a given state with the highest q-value.
        '''
        return self._policy


    @property
    def type(self):
        '''
        The type of type that this cell is.
        '''
        return self._type


    @property
    def max(self):
        '''
        Returns the index of the highest q-value. This index corresponds to
        the most valuable action.
        :returns: index of highest q-value
        '''
        return self._max


    def get_qValue(self, i):
        '''
        Returns the q-value for performing action i in the current field.
        :param: i: the action we want the q-value of
        '''
        return self._qValues[i]


    def set_qValue(self, idx, val, Gridworld):
        '''
        Sets the q-Value for a given action. Checks if new q-Value is higher than q-values
        for all other sections. If so, marks this one as highest value and sets policy
        to this action.
        If this new highest value is for a different action than the one before, set
        convergence in the Gridworld to false.
        :param: idx: the index of the action we want to set the value for
        :param: val: the value we want to save
        :param: Gridworld: the gridworld we operate in
        '''
        # save the old maximum
        old_max = self.get_qValue(self._max)
        # assign the value that should be updated
        self._qValues[idx] = val

        # if new value is bigger than the old maximum
        if val > old_max:
            # if the action has not been the maximal action before
            # assign this action and the index to be the highest
            if idx != self._max:
                self._max = idx
                self._policy = idx
                Gridworld.converged = False #policy changed, so no convergence
        # if the value is smaller than the old maximum
        # we need to check if this was the old maximum and change that
        elif val < old_max:
            if idx == self._max:
                # find the new highest value and set it as the maximum index
                new_highest_qVal = max(self._qValues)
                new_index = self._qValues.index(new_highest_qVal)
                self._max = new_index
                Gridworld.converged = False #policy changed, so no convergence


    @property
    def max_qValue(self):
        '''
        The highest q-Value in our cell.
        '''
        val = self.get_qValue(self._max)
        return (val)

    def get_print_string(self):
        '''
        Returns the qValues as fairly formatted strings
        :return: two lines of q-Values for strings
        '''

        #get values for up and down
        pristri1 =  str(self.get_qValue(0)) + " , " + str(self.get_qValue(1))
        #get values for left and right
        pristri2 =  str(self.get_qValue(2)) + " , " + str(self.get_qValue(3))
        return " (" + pristri1 + ") " + "\n" + " (" + pristri2 + ") "
