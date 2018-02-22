import fileinput

class Gridworld:
    '''
    Finds policies for the best way from each field
    of a grid by applying temporal difference learing.
    '''

    def __init__(self):
        self.actions = ["up", "down", "left", "right"]
        self.processingMode = "m"
        self.grid = ""
        self.targetpolicy = []
        self.behaviorpolicy = []
        self.values = []
        self.epsilon = 0
        self.alpha = 0
        #TODO decide if we want to initialize with 0 instead
        # of these values (which would probably be 'cleaner programming')
        self.GAMMA = 1
        self.REWARD = -0.04
        self.PITFALL = -1
        self.GOAL = 1
        self.ITERATIONS = 1
