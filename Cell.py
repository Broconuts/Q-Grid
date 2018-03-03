import numpy as np
from enum import IntEnum

class Action:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Cell:
    '''
    Conceptualizes a cell of Gridworld with the required properties of such a type.
    A cell has a type (either free, obstacle, pitfall or exit), a policy (greedy action), 
    a value for each action, and the index of the highest value (for ease of access).
    '''

    def __init__(self, actions, type):
        self._type = type
        self._policy = 0
        self._qValues = np.zeros(actions)
        self._max = 0 # idx of maximal qValue


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
        self._qValues[idx] = val
        
        if val > self.get_qValue(self._max) and idx != self._max:
            self._max = idx
            self._policy = idx
            Gridworld.converged = False


    @property
    def max_qValue(self):
        '''
        The highest q-Value in our cell.
        '''
        val = self.get_qValue(self._max)
        return (val)