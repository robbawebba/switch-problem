class State(object):

    def __init__(self, *args):
      super(State, self).__init__()
      self.state = args

    def containsEngine(self, track):
      return self.state[track-1].count('*')
