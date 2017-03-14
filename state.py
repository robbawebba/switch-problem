import numbers
# The state object that represents both the goal states and the current/initial states
class State(object):
    # constructor
    # To create initial and current states: the arguments should be a variable number
    #                                       of lists, and each list (track) should contain a
    #                                       list of characters representing the cars
    #                                       located at that particular track
    # To create goal states: the first argument should be the track number of the goal
    #                        track, the rest should be a variable number of empty
    #                        lists (one empty list for each track)
    def __init__(self, *args):
      super(State, self).__init__()
      if isinstance(args[0], numbers.Number): # checks if the first argument is a number (only goal states have numbers)
          self.goal = args[0]
          self.state = args[1:]
      else: #for regular states
          self.state = args
      self.f = -1 # initialize the f(n) function to -1 for the informed search function
      self.pathCost = -1 # initialize the path cost for this node to -1 for the informed search function

    # helper function to determine if the engine is located in the given track
    def containsEngine(self, track):
      return self.state[track-1].count('*')
