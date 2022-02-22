import dsc40graph

def biggest_descendent(graph, root, value):
    dfs(graph,root,value)
    return value


def dfs(graph, u, value , status=None):
    if status == None:
        status = {node : 'undiscovered' for node in graph.nodes}

    status[u] = 'pending'

    max_list = []
    max_num = 0
    max_length = 0
    for v in graph.neighbors(u):
        if status[v] == 'undiscovered':
           max_list.append(dfs(graph, v, value, status))
    max_length = len(max_list)
    if( max_length > 1):
        max_num = max(max_list)
    status[u] = 'visited'
    if(max_num > value[u]):
        value[u] = max_num
    return value[u]
    #print(value[u])


#edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
#g = dsc40graph.DirectedGraph()
#for edge in edges: g.add_edge(*edge)

#value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
#print(biggest_descendant(g, 1, value))