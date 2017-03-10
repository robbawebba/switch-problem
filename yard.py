class Yard:
  def __init__(self, connections, state):
    self.connections = connections
    self.state = state

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
