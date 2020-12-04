# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import util

class SearchProblem:

    def getStartState(self):

        util.raiseNotDefined()

    def isGoalState(self, state):

        util.raiseNotDefined()

    def getSuccessors(self, state):

        util.raiseNotDefined()

    def getCostOfActions(self, actions):

        util.raiseNotDefined()


def tinyMazeSearch(problem):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):


    dego_man = util.Stack()
    visited = []
    actionList = []
    dego_man.push((problem.getStartState(), actionList))
    while dego_man:
        node, actions = dego_man.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                dego_man.push((coordinate, nextActions))
    return []

# def breadthFirstSearch(problem):
#
#     dego_man = util.Queue()
#     visited = []
#     actionList = []
#
#     dego_man.push((problem.getStartState(), actionList))
#     while dego_man:
#         node, actions = dego_man.pop()
#         if not node in visited:
#             visited.append(node)
#             if problem.isGoalState(node):
#                 return actions
#             for successor in p
# roblem.getSuccessors(node):
#                 coordinate, direction, cost = successor
#                 nextActions = actions + [direction]
#                 dego_man.push((coordinate, nextActions))
#     return []

def uniformCostSearch(problem):
    dego_man = util.PriorityQueue()
    visited = []
    actionList = []
    dego_man.push((problem.getStartState(), actionList), problem)
    while dego_man:
        node, actions = dego_man.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                dego_man.push((coordinate, nextActions), nextCost)
    return []

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    dego_man = util.PriorityQueue()
    visited = []
    actionList = []
    dego_man.push((problem.getStartState(), actionList), heuristic(problem.getStartState(), problem))
    while dego_man:
        node, actions = dego_man.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions) + \
                               heuristic(coordinate, problem)
                dego_man.push((coordinate, nextActions), nextCost)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
