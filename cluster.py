import dsc40graph
from collections import deque


def cluster(graph, weights, level):

    non_frozen_clusters = full_bfs(graph,weights, level)
    return frozenset(non_frozen_clusters)




def full_bfs(graph, weights, level):
    status = {node: 'undiscovered' for node in graph.nodes}
    #counter =      # alternative approach is to change values in status and increment counter based on connected components
    clusters = list([])
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            clusters.append(bfs(graph, node, weights, level,  status))
    return clusters


def bfs(graph, source, weights, level, status=None):

    temp_frs_set = set()
    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}

    status[source] = 'pending'
    temp_frs_set.add(source)
    pending = deque([source])

    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            if (status[v] == 'undiscovered') and (weights(u,v) >= level):
                temp_frs_set.add(v)
                status[v] = 'pending'
                pending.append(v)
        status[u] = 'visited'


    return frozenset(temp_frs_set)