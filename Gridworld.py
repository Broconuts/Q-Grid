import manageIO;


class Gridworld:
    '''
    Finds policies for the best way from each field
    of a grid by applying temporal difference learing.
    '''

    def __init__(self):
        self.actions = ["up", "down", "left", "right"]
        self.processingMode = "m"
        self.grid = [['F', 'F', 'F', 'E'], ['F', 'O', 'F', 'P'], ['F', 'F', 'F', 'F']]
        self.targetpolicy = []
        self.behaviorpolicy = []
        self.values = []
        self.epsilon = 0
        self.alpha = 0
        self.GAMMA = 1
        self.REWARD = -0.04
        self.PITFALL = -1
        self.GOAL = 1
        self.ITERATIONS = 1

    def initializePolicy(self, value):
        '''
        initializes a policy for a grid with a value for all possible actions
        :param value: the default value every action gets in every state
        :return: initialized policy
        '''

        # initialize with zero to create array of size we want
        policy = [[0 for x in range(len(self.grid[0]))] for y in range(len(self.grid))]

        # iterate over array
        for i in range(len(self.grid)):

            for j in range(len(self.grid[0])):
                # if we have a state-field: init dict with actions with the param value
                if(self.grid[i][j] == "F"):
                    policy[i][j] = {"up": value,
                                          "down": value,
                                          "left": value,
                                          "right": value}
                # goal, pitfall and obstacle get value None
                else:
                    policy[i][j] = None

        return policy


if __name__ == '__main__':
    test = Gridworld();
    #manageIO.readUserInput(test); Habe ein Grid als default gesetzt
    test.targetpolicy = test.initializePolicy(0.25)
    test.behaviorpolicy = test.initializePolicy(0)
