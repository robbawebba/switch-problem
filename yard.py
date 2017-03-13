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
