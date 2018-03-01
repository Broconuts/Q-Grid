import manageIO;
import calculate;

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
        self.converged = False
        self.epsilon = 0.5
        self.alpha = 0.5
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


    def runEpisode(self):
        '''
        Simulates an episode from start (currently always the bottom right corner) to
        finish (reaching a goal state) and updates the knowledge (in form of the q-values)
        in the process. How the episode is run depends on the user's choice.
        manual: shows the user each step and the updated q-value-array for each step
        automatic: runs entire episode without output until end of episode is reached
        (whether or not it then prints the q-value-function depends on whether the user
        has chosen the single-episode mode or the full-automatic mode).
        '''

        # set the current state to its initial position (bottom left corner)
        currentstate = (len(self.grid) - 1, 0)

        iterations = 0
        # run this until we reach a goalstate
        while self.grid[currentstate[0]][currentstate[1]] != "E":
            # determine action (epsilon-soft)
            action = calculate.ActionSelection(self, currentstate)
            # determine the next state given our current state and the chosen action
            nextstate = calculate.nextState(self, currentstate, action)
            # update the value function for this state-action pair
            calculate.qUpdate(self, currentstate, action, nextstate)
            # for manual processing: print the now updated value function
            #TODO: this if-condition may increase runtime noticeably. Check this.
            if self.processingMode == "m":
                print("Updated q-values:")
                manageIO.printValues(self)
            # move from current state to next state
            currentstate = nextstate
            iterations = iterations + 1

            print("Number of iterations: " + str(iterations))


if __name__ == '__main__':
    test = Gridworld();
    #manageIO.readUserInput(test); Habe ein Grid als default gesetzt
    test.targetpolicy = test.initializePolicy(0.25)
    test.behaviorpolicy = test.initializePolicy(0)
    # initialize action-value function with 0
    test.values = [[[0 for x in range(len(test.grid[0]))] for y in range(len(test.grid))] for z in range(len(test.actions))]

    # if fully automatic processing mode is chosen
    if test.processingMode == "a":
        # run episodes until stopping criterion (convergence) is met
        while not test.converged:
            test.runEpisode()
            # checks if policies converge and if they don't updates policy
            calculate.updatePolicy(test)

        print("The suggested q-values after convergence of policies are:")
        manageIO.printValues(test.values)

    # if semi-automatic or manual processing mode is chosen
    else:
        # run initial episode
        test.runEpisode()
        # update policy accordingly
        calculate.updatePolicy(test)

        # ask the user after each episode if he or she wants to continue
        while manageIO.continuationRequest() is True:
            test.runEpisode()
            calculate.updatePolicy(test)
            # if convergence has occurred, notify user
            # he or she may continue anyway if desired
            if test.converged:
                print("This episode did not change the recommended policies.")
            else:
                print("Policy has been updated.")

        print("The suggested q-values after convergence of policies are:")
        manageIO.printValues(test.values)