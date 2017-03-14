from yard import Yard
from state import State
import sys

yard1 = Yard((1,2))
state1 = State(['a','*','b'],['c','d'])

yard2 = Yard((1,5), (1,2), (2,3), (2,4))
state2 = State(['*'], ['d'], ['b'], ['a','e'], ['c'])
goal2 = State(1, ['*','a','b','c','d', 'e'], [], [], [])

yard3 = Yard((1,2),(1,3))
state3 = State(['*'],['a'],['b'])
goal3 = State(1, ['*','a','b'], [], [])

yard4 = Yard((1,2),(1,3),(1,4))
state4 = State(['*'],['a'],['b','c'],['d'])
goal4 = State(1, ['*','a','b','c','d'], [], [], [])
yard5 = Yard((1,2),(1,3),(1,4))
state5 = State(['*'],['a'],['c','b'],['d']) # Note c and b out of order
goal5 = State(1, ['*','a','b','c','d'], [], [], [])

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
    return stateCopy

def expand(yard, state):
    actions = possibleActions(yard, state)
    expansion = []
    for action in actions:
        expansion.append(result(yard, action, state))

    return expansion

def goalTest(state, goal):
    return state.state[0] == goal.state[goal.goal-1]

def dls(yard, state, goal, limit):
    path = []
    def recursiveDLS(yard, state, goal, limit):
        if goalTest(state, goal):
            path.append(state.state)
            return state
        elif limit == 0:
            return "limit"
        else:
            limitReached = False
            for child in expand(yard, state):
                result = recursiveDLS(yard, child, goal, limit-1)
                if result == "limit":
                    limitReached = True
                elif result is not None:
                    path.append(state.state)
                    return result
            return "limit" if limitReached else None
    result = recursiveDLS(yard, state, goal, limit)
    if result == "limit":
        return result
    else:
        return path

def blindSearch(yard, state, goal):
    for depth in range(sys.maxsize):
        result = dls(yard, state, goal, depth)
        if result != "limit":
            return result

def heuristic(yard, state, goalTrack):
    sum = 0
    for track in state.state:
        for car in track:
            if track == state.state[goalTrack-1] # car is in the
                continue
            if yard.adjacent(goalTrack, state.state.index[track])
                sum += 1
            if
    return sum

def recursiveBFS(yard, state, goal, h=None):
    path = []
    def RBFS(yard, state, goal, pathCost, flimit):
        if goalTest(state, goal):
            pathCost+1
            path.append(state.state)
            return state, 0   # (The second value is immaterial)
        children = expand(yard, state)
        # print children
        if len(children) == 0:
            return None, -1
        for child in children:
            child.f = max(pathCost + h(yard, child, goal.goal), state.f)
            # print child.f
        while True:
            # Order by lowest f value
            children.sort(key=lambda child: child.f)
            best = children[0]
            # print best
            # print best.f
            if best.f > flimit:
                return None, best.f
            if len(children) > 1:
                alternative = children[1].f
            else:
                alternative = -1
            result, best.f = RBFS(yard, best, goal, pathCost+1, min(flimit, alternative))
            if result is not None:
                path.append(state.state)
                return result, best.f

    state.f = h(yard,state,goal.goal)
    result, bestf = RBFS(yard, state, goal, 0, sys.maxsize)
    # print result, bestf
    return path

# print blindSearch(yard3, state3, goal3)
# print blindSearch(yard4, state4, goal4)
# print blindSearch(yard5, state5, goal5)
# print blindSearch(yard2, state2, goal2)

print recursiveBFS(yard3, state3, goal3, heuristic)
print recursiveBFS(yard4, state4, goal4, heuristic)
print recursiveBFS(yard5, state5, goal5, heuristic)

print recursiveBFS(yard2, state2, goal2, heuristic)


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
# print state1.state

# print expand(yard1, state1)
# print expand(yard3, state3)
# print expand(yard4, state4)
# print expand(yard5, state5)
