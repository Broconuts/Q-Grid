import manageIO
import calculate
import numpy as np
import Cell


class Gridworld:
    '''
    Finds policies for the best way from each field
    of a grid by applying temporal difference learing.
    '''

    def __init__(self):
        self.actions = ["up", "down", "left", "right"]
        self.processingMode = "s"
        field = [['F', 'F', 'F', 'E'], ['F', 'O', 'F', 'P'], ['F', 'F', 'F', 'F']]
        self.grid = np.zeros((len(field), len(field[0])), dtype=Cell.Cell)
        for r in range(len(field)):
            for c in range(len(field[0])):
                self.grid[r, c] = Cell.Cell(len(self.actions), field[r][c])

        self.converged = False
        self.convergencecriterion = 2
        self.convergencecounter = 0
        self.epsilon = 0.5
        self.alpha = 0.5
        self.GAMMA = 1
        self.REWARD = -0.04
        self.PITFALL = -1
        self.GOAL = 1
        self.ITERATIONS = 1

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
        # TODO: check if a two-dimensional array can be accessed like this
        while self.grid[currentstate[0]][currentstate[1]].type != "E" and self.grid[currentstate[0]][
            currentstate[1]].type != "P":
            # determine action (epsilon-soft)
            action = calculate.selectAction(self, currentstate)
            # determine the next state given our current state and the chosen action
            nextstate = calculate.nextState(self, currentstate, action)
            # update the value function for this state-action pair
            calculate.qUpdate(self, currentstate, action, nextstate)
            # for manual processing: print the now updated value function
            # TODO: this if-condition may increase runtime noticeably. Check this.
            if self.processingMode == "m":
                print("Updated q-values:")
                manageIO.printValues(self)
            # move from current state to next state
            currentstate = nextstate
            iterations = iterations + 1

        print("Number of iterations: " + str(iterations))


    def checkForConvergence(self):
        '''
        Checks if convergence criterion is met.
        :returns: True when convergence criterion is met, False when it is not
        ''' 
        # if episode finished without changing policies, increase
        # convergence counter
        if self.converged == True:
            self.convergencecounter += 1
        # if a policy was changed during an episode, reset convergence counter
        else:
            self.convergencecounter = 0
        
        # if the amount of episodes that have finished without changing policies
        # matches the set criterion when we deem the policies to have converged,
        # return True
        if self.convergencecounter == self.convergencecriterion:
            return True
        
        return False


if __name__ == '__main__':
    gw = Gridworld()
    # manageIO.readUserInput(gw); Habe ein Grid als default gesetzt

    # if fully automatic processing mode is chosen
    if gw.processingMode == "a":
        # run episodes until stopping criterion (convergence) is met
        while not gw.checkForConvergence():
            # setting converged to True before each episode. Will be set
            # to false as soon as a single greedy policy is changed
            gw.converged = True
            gw.runEpisode()

        print("The suggested q-values after convergence of policies are:")
        manageIO.printQValues(gw)
        manageIO.printPolicy(gw)

    # if semi-automatic or manual processing mode is chosen
    else:
        # run initial episode
        gw.runEpisode()

        # ask the user after each episode if he or she wants to continue
        while manageIO.continuationRequest() is True:
            # setting converged to True before each episode. Will be set
            # to false as soon as a single greedy policy is changed
            gw.converged = True
            gw.runEpisode()

            # if convergence has occurred, notify user
            # he or she may continue anyway if desired
            if gw.checkForConvergence():
                print("Your set convergence criterion has been met.")
            else:
                print("Policy has been updated.")
            manageIO.printPolicy(gw)

        print("The suggested q-values after convergence of policies are:")
        manageIO.printQValues(gw)
