#
# Maintains and explores a directed graph.
# Each node keeps a list of adjacent nodes.
# Traversals end on nodes that have no adjacent nodes.
#
import random
import numpy

class Digraph(object):
  def __init__(self):
    self.nodes = dict()

  def AddNode(self, node, nextnodes):
    self.nodes[node] = nextnodes

  def GetNextNodes(self, nodeid):
    return self.nodes[nodeid]

  def BreadthFirstOrder(self, start):
    order = []
    visited = set()
    queue = [start]
    while queue:
      node = queue.pop(0)
      if node not in visited:
        order.append(node)
        visited.add(node)
        queue.extend(self.GetNextNodes(node))
    return order

  def DepthFirstOrder(self, start):
    order = []
    visited = set()
    stack = [start]
    while stack:
      node = stack.pop()
      if node not in visited:
        order.append(node)
        visited.add(node)
        stack.extend(self.GetNextNodes(node))
    return order

  def FindAllPaths(self, start, path=[]):
    path = path + [start]
    nextnodes = self.GetNextNodes(start)
    if not nextnodes:
      return [path]
    paths = []
    for node in nextnodes:
      if node not in path:
        newpaths = self.FindAllPaths(node, path)
        for newpath in newpaths:
          paths.append(newpath)
    return paths

  def PrintAllPaths(self, start, verbose):
    lengths = []
    paths = self.FindAllPaths(start)
    for path in paths:
      lengths.append(len(path))
      if verbose:
        print path
    PrintLengthStats(lengths)

  def PrintDot(self):
    print "digraph {"
    for node in sorted(list(self.nodes), key=int):
      for nextnode in sorted(self.GetNextNodes(node), key=int):
        print "  " + node + " -> " + nextnode + ";"
    print "}"

  def RandomWalk(self, start):
    walk = []
    node = start
    while True:
      walk.append(node)
      nextnodes = self.GetNextNodes(node)
      if not nextnodes:
        break
      node = random.choice(nextnodes)
    return walk

  def PrintRandomWalks(self, start, count, verbose):
    lengths = []
    for i in range(count):
      walk = self.RandomWalk(start)
      lengths.append(len(walk))
      if verbose:
        print walk
    PrintLengthStats(lengths)

def PrintLengthStats(lengths):
  print "count: " + str(len(lengths))
  print "minimum length: " + str(min(lengths))
  print "25%ile length: " + str(int(numpy.percentile(lengths, 25)))
  print "median length: " + str(int(numpy.median(lengths)))
  print "75%ile length: " + str(int(numpy.percentile(lengths, 75)))
  print "maximum length: " + str(max(lengths))
