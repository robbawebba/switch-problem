class State(object):

    def __init__(self, *args):
      super(State, self).__init__()
      self.state = args

    def containsEngine(self, track):
      return self.state[track-1].count('*')

    def left(self, frm, to):
        if self.containsEngine(frm) or self.containsEngine(to):
          self.state[to-1].append(self.state[frm-1].pop(0))
          return self.state

    def right(self, frm, to):
        if self.containsEngine(frm) or self.containsEngine(to):
          self.state[to-1].insert(0,(self.state[frm-1].pop()))
          return self.state
