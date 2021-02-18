# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
# Your objective is to determine the length of the loop. 
# Use the next attribute to find the next node: node.next
# Please DO NOT MUTATE nodes

def loop_size(node):
    nodes = dict()
    position = 0 
    actnode = node
    while actnode != None:
        if actnode not in nodes:
            position += 1
            nodes[actnode] = position - 1
        else:
            return position - nodes[actnode]
        actnode = actnode.nex
