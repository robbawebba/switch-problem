from yard import Yard
from state import State
import sys

#################################################
#      State Definitions
#################################################
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

#################################################
#      Problem 1: Possible Actions
#################################################
# Input: a yard and a state
# Output: a list of possible actions in the given yard for the current state provided.
# Actions produced are in the form of "DIRECTION FROM TO", separated by spaces
def possibleActions(yard, state):
  engine = 0 # track number where the engine is located
  actionsList = [] # list of possible actions to return
  for track in range(1,len(state.state)): # find the location of the engine
      if state.containsEngine(track):
          engine = track
  for x in yard.connections: # iterate through all connections
    if x[0] == engine: # If the engine is located in left track of this connection
        actionsList.append("right " + str(engine) + " " + str(x[1]))
        if state.state[x[1]-1]: # check if the right track is empty (since we can't move cars from an empty track)
            actionsList.append("left " + str(x[1]) + " " + str(engine))
    elif x[1] == engine: # If the engine is located in right track of this connection
        actionsList.append("left " + str(engine) + " " + str(x[0]))
        if state.state[x[0]-1]: # check if the left track is empty (since we can't move cars from an empty track)
            actionsList.append("right " + str(x[0]) + " " + str(engine))
  return actionsList

#################################################
#      Problem 2: result
#################################################
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

#################################################
#      Problem 3: expand
#################################################
# Input:
# Output: 
def expand(yard, state):
    actions = possibleActions(yard, state)
    expansion = []
    for action in actions:
        expansion.append(result(yard, action, state))

    return expansion

def goalTest(state, goal):
    return state.state[goal.goal-1] == goal.state[goal.goal-1]

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
# Heuristic function for the informed search. This heuristic is admissible
# Scoring scheme:
#  Add 0 if in the goal track AND car is in the correct position
#  If the car is in the goal track BUT is x positions away from it's goal position in the track, add x to sum
#  If the car is in a track adjacent to the goal track, then add 1 (the minimum distance the car would have to move to get to the goal track)
#  If the car is none of the above, then add 2, since there would be a minimum of 2 moves for any car to reach the goal track from anywhere else
def heuristic(yard, state, goal):
    sum = 0
    for track in state.state:
        for car in track:
            if track == state.state[goal.goal-1]: # car is in the goal track
                if track.index(car) == goal.state[goal.goal-1].index(car): # car is in the goal track AND is in the correct position
                    continue # Don't add anything
                else: # add the distance of the car from it's goal position to the sum
                    sum = sum + abs(track.index(car)+1 - goal.state[goal.goal-1].index(car))
            elif yard.adjacent(goal.goal, state.state.index(track)): #if the car is in a track adjacent to the goal track
                sum = sum + 1 # Add 1 (minimum moves for a car to make it to the goal track)
            else: # if car is in a track that's not adjacent to the goal track
                sum = sum + 2 # Add 2 (minimum moves for a car to make it to the goal track when not adjacent to it)
    return sum

def recursiveBFS(yard, state, goal, h=None):
    path = [] # list ot keep track of path cost
    def RBFS(yard, state, goal, pathCost, flimit):
        if goalTest(state, goal): # solution found
            print "GOAL FOUND"
            pathCost+1
            path.append(state.state)
            return state, 0
        children = expand(yard, state) ## expansion of children
        if len(children) == 0:
            return None, sys.maxsize
        for child in children: #calculate f(n) for ecery child, save it to child.f
            print h(yard, child, goal)
            child.f = max(pathCost + h(yard, child, goal), state.f)

        while True:
            print "in loop"
            # Order by lowest f value
            children.sort(key=lambda child: child.f)
            best = children[0]
            print best
            # print best
            # print best.f
            if best.f > flimit:
                return None, best.f
            if len(children) > 1:
                alternative = children[1].f
            else:
                alternative = sys.maxsize
            result, best.f = RBFS(yard, best, goal, pathCost+1, min(flimit, alternative))
            print best.f, best.state
            if result is not None:
                print "HERE"
                path.append(state.state)
                return result, best.f

    state.f = h(yard,state,goal)
    result, bestf = RBFS(yard, state, goal, 0, sys.maxsize)
    return path


#################################################
#      Problem 1 Tests
#################################################
# print possibleActions(yard1, state1)
# print possibleActions(yard2, state2)
# print possibleActions(yard3, state3)
# print possibleActions(yard4, state4)
# print possibleActions(yard5, state5)

#################################################
#      Problem 3 Tests
#################################################
# print expand(yard1, state1)
# print expand(yard2, state2)
# print expand(yard3, state3)
# print expand(yard4, state4)
# print expand(yard5, state5)

#################################################
#      Problem 4 Tests
#################################################
# print blindSearch(yard3, state3, goal3)
# print blindSearch(yard4, state4, goal4)
# print blindSearch(yard5, state5, goal5)
# print blindSearch(yard2, state2, goal2)

#################################################
#      Problem 6 Tests
#################################################
# print recursiveBFS(yard3, state3, goal3, heuristic)
# print recursiveBFS(yard4, state4, goal4, heuristic)
# print recursiveBFS(yard5, state5, goal5, heuristic)
# print recursiveBFS(yard2, state2, goal2, heuristic)
