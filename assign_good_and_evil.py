from collections import deque
import dsc40graph


def assign_good_and_evil(graph):
    return  full_bfs(graph)


def full_bfs(graph):
    status = {node: 'undiscovered' for node in graph.nodes}

    result = 1
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            result = bfs(graph, node, status)

        if(result == None):
            return None


    dict = {}

    counter = 0
    for u in graph.nodes:
        dict[u] = status[u]
        counter+=1

    return dict

def bfs(graph, source, status):

    counter = 1

    status[source] = 'good'
    pending = deque([source])

    while pending:
        u = pending.popleft()

        for v in graph.neighbors(u):

            if((status[v] != 'undiscovered') & (status[u] == status[v])):
                return None

            if status[v] == 'undiscovered':
                if counter % 2 == 1:
                    status[v] = 'evil'
                else:
                    status[v] = 'good'
                pending.append(v)

        counter += 1
    return 1



#example_graph = dsc40graph.UndirectedGraph()
#example_graph.add_edge('Michigan', 'OSU')
#example_graph.add_edge('USC', 'OSU')
#example_graph.add_edge('USC', 'UCLA')
#example_graph.add_node('UCSD')

#print(assign_good_and_evil(example_graph))
