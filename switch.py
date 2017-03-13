from yard import Yard
from state import State

yard1 = Yard((1,2))
state1 = State(['a','*','b'],['c','d'])

yard3 = Yard((1,2),(1,3))
state3 = State(['*'],['a'],['b'])
goal3 = State(['*','a','b'], [], [])

yard4 = Yard((1,2),(1,3),(1,4))
state4 = State(['*'],['a'],['b','c'],['d'])
goal4 = State(['*','a','b','c','d'], [], [], [])
yard5 = Yard((1,2),(1,3),(1,4))
state4 = State(['*'],['a'],['c','b'],['d']) # Note c and b out of order
goal5 = State(['*','a','b','c','d'], [], [], [])

def possibleActions(yard, state):
  engine = 0 # track number where the engine is located
  actionsList = [] # list of possible actions to return
  for track in range(1,len(state.state)): ## find the location of the engine
      if state.containsEngine(track):
          engine = track
  for x in yard.connections:
    if x[0] == engine:
        actionsList.append("right(" + str(engine) + ", " + str(x[1]) + ")")
        if state.state[x[1]-1]: # only add left-move
            actionsList.append("left(" + str(x[1]) + ", " + str(engine) + ")")
    elif x[1] == engine:
        actionsList.append("left(" + str(engine) + ", " + str(x[0]) + ")")
        if state.state[x[0]-1]:
            actionsList.append("right(" + str(x[0]) + ", " + str(engine) + ")")

  return actionsList




print state1.containsEngine(1)
print state1.containsEngine(2)

print possibleActions(yard1, state1)

print state1.left(2,1)
print state1.right(2,1)

print possibleActions(yard1, state1)
