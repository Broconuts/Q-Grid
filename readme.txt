Implement a program that reads in a grid world file and learns an optimal policy using Q-learning. You can use a fixed start state, i.e. the field (1,1) (bottom left corner), or you can use "exploring starts" and choose the initial state of every episode randomly from the set of all legal starting points. The latter approach leads to faster convergence of the algorithm.
The exploration rate Epsilon for the epsilon-soft-policy should be set by the user. You can decide for yourself whether the Epsilon should decrease with the number of episodes or whether it is fixed. An Epsilon of 1 would mean that the agent explores the grid randomly.


Program must be able to perform the following:

  Reading in Gridfiles
      Program should be able to read the provided files and to transform them into appropriate data structures that can be used by the implementation.

  The code Works
      Program does not crash for regular inputs and performs policy iteration correctly.

  Manual stepwise q-value update for one episode
      The agent takes one step and the updated matrix is shown.

  Automatic q-value update for one episode
      Iteration until the agent ends up in the goal state / in an end-state. If the agent reaches the end state the value matrix and policy matrix are shown.

  Automatic q- value update until convergence
      Agent iterates through multiple episodes until the policy is found in episode n and does not change in episode n+1.


Remark regarding test files:
The Program only has to perform on the 3by4.grid file. It can also be tested on bigger grids but the runtime of the algorithm might be considerably higher.
