__author__ = 'monica_wang'
import heapq
import copy

UNFOUND = 1000000

class Vertex:

    def __init__(self):
        self.label = 0
        self.score = UNFOUND
        self.edges = []

    def setVertex(self, label, score, edges):
        self.label = label
        self.score = score
        self.edges = edges

    def __cmp__(self, other):
        if self.score < other.score:
            return -1
        if self.score == other.score:
            return 0
        if self.score > other.score:
            return 1

    def __repr__(self):
        return "Vertex: "+str(self.label)+" with score: "+str(self.score)

def read_from_file():
    with open('dijkstraData.txt', 'r') as f:
        lines = f.readlines()
        N = len(lines)
        graph = [Vertex() for i in range(N+1)]  # graph index is vertex label

        for line in lines:
            label = int(line.split()[0])
            edges = [ (int(n.split(",")[0]), int(n.split(",")[1])) for n in line.split()[1:]]
            graph[label].setVertex(label, UNFOUND, edges)

        # 1 is source
        graph[1].score = 0
    return graph


if __name__ == "__main__":

    graph = read_from_file()

    visited = set()
    unvisited = []
    # shallow copy
    unvisited = graph[1:]

    heapq.heapify(unvisited)

    while unvisited != []:
        # greedy: get vertex with minimum score
        m = heapq.heappop(unvisited)

        # add m to visited
        visited.add(m.label)

        # compute score for m's connected node
        for c in graph[m.label].edges:
            v, dis = c
            if v in visited:
                pass

            # update score of v
            graph[v].score = min(graph[v].score, graph[m.label].score + dis)

            heapq.heapify(unvisited)

    answers = [7,37,59,82,99,115,133,165,188,197]
    #answers = [80,163,170]
    res = [graph[a].score for a in answers]
    print res




