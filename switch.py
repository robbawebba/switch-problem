from yard import Yard
from state import State
import copy

yard1 = Yard((1,2))
state1 = State(['a','*','b'],['c','d'])

yard2 = Yard((1,5), (1,2), (2,3), (2,4))
state2 = State(['*'], ['d'], ['b'], ['a','e'], ['c'])

yard3 = Yard((1,2),(1,3))
state3 = State(['*'],['a'],['b'])
goal3 = State(['*','a','b'], [], [])

yard4 = Yard((1,2),(1,3),(1,4))
state4 = State(['*'],['a'],['b','c'],['d'])
goal4 = State(['*','a','b','c','d'], [], [], [])
yard5 = Yard((1,2),(1,3),(1,4))
state5 = State(['*'],['a'],['c','b'],['d']) # Note c and b out of order
goal5 = State(['*','a','b','c','d'], [], [], [])

def possibleActions(yard, state):
  engine = 0 # track number where the engine is located
  actionsList = [] # list of possible actions to return
  for track in range(1,len(state.state)): ## find the location of the engine
      if state.containsEngine(track):
          engine = track
  for x in yard.connections:
    if x[0] == engine:
        actionsList.append("right " + str(engine) + " " + str(x[1]))
        if state.state[x[1]-1]: # only add left-move
            actionsList.append("left " + str(x[1]) + " " + str(engine))
    elif x[1] == engine:
        actionsList.append("left " + str(engine) + " " + str(x[0]))
        if state.state[x[0]-1]:
            actionsList.append("right " + str(x[0]) + " " + str(engine))

  return actionsList

# Input: A yard, an action in the form of "DIRECTION FROM TO" (separated by spaces), a state
# Example input: result("right 1 2", state1)
# Output: the new state that would result from applying the action
def result(yard, action, state):
    newState = []
    for track in state.state:
        newState.append(list(track))
    stateCopy = State(*newState)
    actionArgs = action.split(' ')
    if actionArgs[0] == "right":
        yard.right(stateCopy, int(actionArgs[1]), int(actionArgs[2]))
    elif actionArgs[0] == "left":
        yard.left(stateCopy, int(actionArgs[1]), int(actionArgs[2]))
    return stateCopy.state

def expand(yard, state):
    actions = possibleActions(yard, state)
    expansion = []
    for action in actions:
        expansion.append(result(yard, action, state))

    return expansion


# Test containsEngine
# print state1.containsEngine(1)
# print state1.containsEngine(2)

# Test possibleActions
# print possibleActions(yard1, state1)
# print possibleActions(yard3, state3)
# print possibleActions(yard4, state4)
# print possibleActions(yard5, state5)

# print yard1.left(state1,2,1)
# print yard1.right(state1,2,1)
print state1.state

print expand(yard1, state1)
print expand(yard3, state3)
print expand(yard4, state4)
print expand(yard5, state5)
