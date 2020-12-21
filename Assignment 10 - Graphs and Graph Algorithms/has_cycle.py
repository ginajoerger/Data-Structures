from graph import Graph     

def has_cycle(g):
    ''' returns true if the graph is cyclic. returns false if the graph is not cyclic.
        @g: the graph, in our case, it is an Adjacency map

        # Hint: mark visited vertices 
        return: True/False
    '''
    # To do    
    discovered_list = {}
    start = list(g.vertices())[0]
    discovered_list[start] = None
    
    level = [start]
    
    while len(level) > 0:
        next_level = []
        for  i in level:
            for j in g.incident_edges(i):
                x = j.opposite(i)
                if x not in discovered_list:
                    discovered_list[x] = j
                    next_level.append(x)
                elif x in discovered_list:
                    return True
        level = next_level
    return False

def main():
    g1 = Graph(True) # cyclic graph
    va = g1.insert_vertex("A")
    g1.insert_edge(va, va, 0)
    boolean = has_cycle(g1)  # True
    if boolean:
        print("g1 is cyclic (expected)")
    else:
        print("g1 is not cyclic")
    g2 = Graph(True)
    va = g2.insert_vertex("A")
    vb = g2.insert_vertex("B")
    vc = g2.insert_vertex("C")
    vd = g2.insert_vertex("D")
    ve = g2.insert_vertex("E")
    vf = g2.insert_vertex("F")
    g2.insert_edge(va, vb, 1)
    g2.insert_edge(vb, vc, 2)
    g2.insert_edge(vc, vd, 3)
    g2.insert_edge(vd, ve, 4)
    g2.insert_edge(ve, vf, 5)
    g2.insert_edge(vf, va, 6)
    boolean = has_cycle(g2)  # True
    if boolean:
        print("g2 is cyclic (expected)")
    else:
        print("g2 is not cyclic")

    g3 = Graph(True)
    va = g3.insert_vertex("A")
    vb = g3.insert_vertex("B")
    vc = g3.insert_vertex("C")
    vd = g3.insert_vertex("D")
    ve = g3.insert_vertex("E")
    vf = g3.insert_vertex("F")
    g3.insert_edge(va, vb, 1)
    g3.insert_edge(vb, vc, 2)
    g3.insert_edge(vc, vd, 3)
    g3.insert_edge(vd, ve, 4)
    g3.insert_edge(ve, vf, 5)
    boolean = has_cycle(g3)  # False
    if boolean:
        print("g3 is cyclic")
    else:
        print("g3 is not cyclic (expected)")

    g4 = Graph(True)
    va = g4.insert_vertex("A")
    vb = g4.insert_vertex("B")
    vc = g4.insert_vertex("C")
    vd = g4.insert_vertex("D")
    ve = g4.insert_vertex("E")
    vf = g4.insert_vertex("F")
    g4.insert_edge(va, vb, 1)
    g4.insert_edge(va, vc, 2)
    g4.insert_edge(va, vd, 3)
    g4.insert_edge(vd, ve, 4)
    g4.insert_edge(ve, va, 5)
    boolean = has_cycle(g4)  # True
    if boolean:
        print("g4 is cyclic (expected)")
    else:
        print("g4 is not cyclic ")


#main()
