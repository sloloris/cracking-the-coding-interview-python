""" Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """

def find_route(node1, node2):
    to_visit = []
    visited = set()

    current = node1
    while current:
        if current == node2:
            return True
        for child in current.adjacent:
            if child not in visited:
                to_visit.append(child)
        visited.add(current)
        current = to_visit.pop(0)

    return False





if __name__ == "__main__":
    print "nothing yet"