class Yard:
  def __init__(self, *connections):
    self.connections = connections ## connections list
    self.numTracks = 0 # number of tracks in the yard
    for x in self.connections: # Finds the number of tracks (gets the largest track number)
      if x[0] > self.numTracks:
        self.numTracks = x[0]
      if x[1] > self.numTracks:
        self.numTracks = x[1]

    # connectivity matrix - just another way of storing the track connections
    self.matrix = [[0 for x in range(self.numTracks)] for y in range(self.numTracks)]
    for x in self.connections: # populate the connectivity matrix
      self.matrix[x[0]-1][x[1]-1] = 1

  ## Input: The state to manipulate, the track to move a car from, and the track to move the car to
  # output: On success - the new state. On failure: an error message
  def left(self, state, frm, to):
      if state.containsEngine(frm) or state.containsEngine(to): # only move cars from tracks with engines
          for x in self.connections:
              if x[0] == to and x[1] == frm:# check that (to frm) is in the connectivity list
                state.state[to-1].append(state.state[frm-1].pop(0)) # move car to the left
                return state.state
          return "(" + str(to) +", "+str(frm)+") not in connectivity list"
      else:
          return "Engine is not located in either track"

  ## Input: The state to manipulate, the track to move a car from, and the track to move the car to
  # output: On success - the new state. On failure: an error message
  def right(self, state, frm, to):
      if state.containsEngine(frm) or state.containsEngine(to): # only move cars from tracks with engines
          for x in self.connections:
              if x[0] == frm and x[1] == to: # check that (frm to) is in the connectivity list
                state.state[to-1].insert(0,(state.state[frm-1].pop())) # move car to the right
                return state.state
          return "(" + str(frm) +", "+str(to)+") not in connectivity list" # error message
      else:
        return "Engine is not located in either track" # error message

  ## Input: two tracks
  # output: True if the two tracks are adjacent (in the connectivity list), false otherwise
  def adjacent(self, frm, to):
      for x in self.connections:
          if (x[0] == to and x[1] == frm) or (x[1] == to and x[0] == frm): # if the tracks match the connection
              return True
      return False
