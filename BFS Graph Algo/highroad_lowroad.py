# Hasan Mukati
# Algorithms 4102
# Breadth-first search

# Goal: Manipulate graphs to solve complex problems

from graph_util import *

def shortest(roadmap, elevations, start, end):
    """
    Returns the length of the shortest highroad-lowroad path.
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    """

    highLowNodePairs = []
    cities = list(elevations.keys())

    for i in cities:
        roadmap.add_edge(i,i)

    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            if elevations[cities[i]] < elevations[cities[j]]: highLowNodePairs.append((cities[i], cities[j]))
            if elevations[cities[i]] > elevations[cities[j]]: highLowNodePairs.append((cities[j], cities[i]))

    highLowNodePairs = [(start,start),(end,end)] + highLowNodePairs

    pnodes = [i[0] + '|' + i[1] for i in highLowNodePairs]
    pgraph = graph(pnodes)

    for i in range(len(highLowNodePairs)):
        for j in range(i+1, len(highLowNodePairs)):
            if roadmap.is_edge(highLowNodePairs[i][0],highLowNodePairs[j][0]) and roadmap.is_edge(highLowNodePairs[i][1],highLowNodePairs[j][1]):
                pgraph.add_edge(highLowNodePairs[i][0]+'|'+highLowNodePairs[i][1], highLowNodePairs[j][0]+'|'+highLowNodePairs[j][1])

    def bfs(n):

        currentNodes = n
        nextNodes = {}
        dist = 0
        while True:
            dist += 1
            for i in currentNodes:
                for nbr in pgraph.get_neighbors(i):
                    if nbr == start + '|' + start:continue
                    if nbr not in nextNodes: nextNodes[nbr] = 0
                    nextNodes[nbr] += currentNodes[i]

            currentNodes = nextNodes
            nextNodes = {}

            if (end+'|'+end) in currentNodes:
                return dist, currentNodes[(end+'|'+end)]

    result = bfs({start+'|'+start : 1})
    return result[0]

def num_shortest(roadmap, elevations, start, end):
    """
    Returns the number of shortest highroad-lowroad paths
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    """

    highLowNodePairs = []
    cities = list(elevations.keys())

    for i in cities:
        roadmap.add_edge(i,i)

    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            if elevations[cities[i]] < elevations[cities[j]]: highLowNodePairs.append((cities[i], cities[j]))
            if elevations[cities[i]] > elevations[cities[j]]: highLowNodePairs.append((cities[j], cities[i]))

    highLowNodePairs = [(start,start),(end,end)] + highLowNodePairs

    pnodes = [i[0] + '|' + i[1] for i in highLowNodePairs]
    pgraph = graph(pnodes)

    for i in range(len(highLowNodePairs)):
        for j in range(i+1, len(highLowNodePairs)):
            if roadmap.is_edge(highLowNodePairs[i][0],highLowNodePairs[j][0]) and roadmap.is_edge(highLowNodePairs[i][1],highLowNodePairs[j][1]):
                pgraph.add_edge(highLowNodePairs[i][0]+'|'+highLowNodePairs[i][1], highLowNodePairs[j][0]+'|'+highLowNodePairs[j][1])

    def bfs(n):

        currentNodes = n
        nextNodes = {}
        dist = 0
        while True:
            dist += 1
            for i in currentNodes:
                for nbr in pgraph.get_neighbors(i):
                    if nbr == start + '|' + start:continue
                    if nbr not in nextNodes: nextNodes[nbr] = 0
                    nextNodes[nbr] += currentNodes[i]

            currentNodes = nextNodes
            nextNodes = {}

            if (end+'|'+end) in currentNodes:
                return dist, currentNodes[(end+'|'+end)]

    result = bfs({start+'|'+start : 1})
    return result[1]