__author__ = 'monica_wang'

import random
import time
import math
from copy import deepcopy

class ContractedNode:
    ''' Represent node in contracted graph
        - nodes: a list of contracted vertices
        - edge: list of vertices 'node' adjacent to
    '''
    def __init__(self, node, edge):
        self.node = node
        self.edge = edge

    def contract(self, other):
        self.node += other.node
        self.edge = [n for n in self.edge + other.edge if n not in self.node]

    def __str__(self):
        return "Contracted node with node: ",self,node," edge: ",self.edge

def cut(graph):
    if len(graph) == 2:
        return graph
    else:
        rand_pick = random.choice(graph)
        merge_node = random.choice(rand_pick.edge)
        merge_pick = [i for i in graph if merge_node in i.node]
        try:
            rand_pick.contract(merge_pick[0])
        except IndexError:
            print "cannot find adjacent node"
            exit(1)
        graph.remove(merge_pick[0])
        return cut(graph)

def min_cut(graph):
    n = len(graph)
    if n < 2:
        return 0

    #numTrails = int(n*n*math.log(n))
    numTrails = 10
    min_cross = len(graph[0].edge)
    out = graph
    for i in range(numTrails):
        trial = cut(deepcopy(graph))
        cuts = len(trial[0].edge)
        if cuts < min_cross:
            min_cross = cuts
            out = trial
    return out, min_cross

graph = []
with open("kargerMinCut.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        nums = [int(i) for i in line.strip().split()]
        if len(nums) > 0:
            node = ContractedNode([nums[0]], nums[1:])
            graph.append(node)

out, min_cross = min_cut(graph)
print "out: ",out
print "min_cross: ",min_cross



