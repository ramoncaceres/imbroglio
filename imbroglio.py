#!/usr/bin/env python
#
# Explores Edward Gorey's "The Raging Tide: or, The Black Doll's Imbroglio"
#
import argparse
import digraph
import imbroglio_lib as lib

# Assumes input in the form of 4 consecutive lines per page, e.g., for page 7:
# 7
# Figbash threw an antimacassar over Skrump.
# If you feel he was right to do this, turn to 9.
# If you think he was wrong, turn to 6.
def ReadText(book, graph):
  f = open('imbroglio.txt', 'r')
  line = f.readline()
  while line != '':  # not end of file
    if line.strip('\n').isdigit():  # number on a line by itself
      pagenum = line.strip('\n')
      story = f.readline().strip('\n')
      choice0 = f.readline().strip('\n')
      choice1 = f.readline().strip('\n')
      book.AddPage(pagenum, story, choice0, choice1)
      graph.AddNode(pagenum, lib.NextPageNumbers(choice0, choice1))
    line = f.readline()

book = lib.Book()
graph = digraph.Digraph()
ReadText(book, graph)

parser = argparse.ArgumentParser(description="Explores Edward Gorey's 'The Raging Tide: or, The Black Doll's Imbroglio'.")
parser.add_argument("--verbose", help="verbose", action="store_true")
group = parser.add_mutually_exclusive_group()
group.add_argument("--prompt", help="prompt for story choices", action="store_true")
group.add_argument("--tell", help="tell a random story", action="store_true")
group.add_argument("--echo", help="echo the full text of the book", action="store_true")
group.add_argument("--breadth", help="traverse the graph in breadth-first order", action="store_true")
group.add_argument("--depth", help="traverse the graph in depth-first order", action="store_true")
group.add_argument("--dot", help="print the graph in DOT format", action="store_true")
group.add_argument("--paths", help="find all paths in the graph", action="store_true")
group.add_argument("--walks", help="do random walks on the graph", type=int)

args = parser.parse_args()
if args.prompt:
  book.PromptForStory()
elif args.tell:
  book.TellStory(graph.RandomWalk('1'), args.verbose)
elif args.echo:
  book.EchoText()
elif args.breadth:
  print graph.BreadthFirstOrder('1')
elif args.depth:
  print graph.DepthFirstOrder('1')
elif args.dot:
  graph.PrintDot()
elif args.paths:
  graph.PrintAllPaths('1', args.verbose)
elif args.walks:
  graph.PrintRandomWalks('1', args.walks, args.verbose)
else:
  parser.print_help()
