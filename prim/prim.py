__author__ = 'monica_wang'
import sys
import mheapq

filename = "edges.txt"

class Vertex:

    def __init__(self, label):
        self.label = label
        self.score = sys.maxint
        self.edges = []

    def setVertex(self, label, score, edges):
        self.label = label
        self.score = score
        self.edges = edges

def primHeap(filename):
    with open(filename, 'r') as f:
        V, E = f.readline().split()
        V, E,  = int(V), int(E)

        # Construct graph
        graph = [Vertex(i) for i in range(V+1)] # graph index is same as vertex label, provides mapping between label and vertex
        for line in f.readlines():
            v1, v2, w = line.split()
            v1, v2, w = int(v1), int(v2), int(w)
            graph[v1].edges.append((v2, w))
            graph[v2].edges.append((v1, w))

        # Pick first vertex
        for e in graph[1].edges:
            v, dis = e
            graph[v].score = dis

        # V is reordered as heap, but order in graph stays, can be used as mapping
        totalDis = 0
        heap = graph[2:]
        processed = set([1])

        # Bookkeeper: mapping of vertex to pos in heap
        map = {}
        for i in range(2, len(graph)):
            map[i] = i-2

        mheapq.heapify(heap, map)

        while heap != []:
            vertexU = mheapq.heappop(heap, map)
            totalDis += vertexU.score
            processed.add(vertexU.label)

            for e in vertexU.edges:
                v, dis = e
                if v not in processed and dis < graph[v].score:
                    graph[v].score = dis
                    pos = map[v]
                    mheapq._siftdown(heap, 0, pos, map)
        return totalDis

def prim(filename):
    with open(filename, 'r') as f:
        V, E = f.readline().split()
        V, E,  = int(V), int(E)

        graph = [[] for i in range(V+1)]
        for line in f.readlines():
            v1, v2, w = line.split()
            v1, v2, w = int(v1), int(v2), int(w)
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))

        X = set([1])
        T = 0

        while len(X) != V:
            min_weight = sys.maxint
            closest_v = None

            for v in X:
                for e in graph[v]:
                    if e[0] not in X:
                        if e[1] < min_weight:
                            min_weight = e[1]
                            closest_v = e[0]
            X.add(closest_v)
            T += min_weight
        return T


import time
t1 = time.time()
result1 = primHeap(filename)
print "result for heap implementation: ", result1, " time: ", time.time() - t1

t2 = time.time()
result2 = prim(filename)
print "result from naive implementation: ", result2, " time: ", time.time() - t2





