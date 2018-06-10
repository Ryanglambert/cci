class DirectedNode(object):
    def __init__(self, name):
        self.name = name
        self.next = []
        self.previous = []

    def __repr__(self):
        return str(self.__class__) + '({})'.format(self.name)

    def add_next(self, name):
        new_node = DirectedNode(name)
        new_node.previous.append(self)
        self.next.append(new_node)
        return new_node

    def add_previous(self, name):
        new_node = DirectedNode(name)
        new_node.next.append(self)
        self.previous.append(new_node)
        return new_node

    def attach_previous(self, node):
        self.previous.append(node)

    def attach_next(self, node):
        self.next.append(node)


def is_directed_route(origin_node: DirectedNode, dest_node: DirectedNode):
    "checks for a route form origin node as directed to dest_node"
    # OMG recursion in python noooooo

    # one way to describe this in a simple verbal way is:
    # Starting at origin_node, let's return True if we bump into dest_node
    # If we don't, then what about if we start at dest_node?

    # should go both ways since we didn't specify whether or
    # not we cared which node was the origin

    # this is a depth first search
    if dest_node in origin_node.next:
        return True
    else:
        for node in origin_node.next:
            return is_directed_route(node, dest_node)
    return False


def is_route_either_way(node1: DirectedNode, node2: DirectedNode):
    "checks for a route to and from each node to the other"
    first_route_present = is_directed_route(node1, node2)
    if first_route_present:
        return True
    second_route_present = is_directed_route(node2, node1)
    if second_route_present:
        return True
    return False

