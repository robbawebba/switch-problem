import numbers

class State(object):

    def __init__(self, *args):
      super(State, self).__init__()
      if isinstance(args[0], numbers.Number):
          self.goal = args[0]
          self.state = args[1:]
      else:
          self.state = args
      self.f = -1
      self.pathCost = -1

    def containsEngine(self, track):
      return self.state[track-1].count('*')
