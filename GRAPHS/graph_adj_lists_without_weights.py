def create_vertex(v):
    global graph
    global vertices_num

    if v in graph:
        print(f"The vertex {v} already exists in graph ")
    else:
        graph[v] = []
        vertices_num = vertices_num + 1

def link_vertices(v1,v2):
    global graph 
    # First check if vertices exists in graph or not 
    if v1 not in graph:
        print(f"The vertex {v1} not exists in graph ")
    elif v2 not in graph:
        print(f"The vertex {v2} not exists in graph ")
    else:
        graph[v1].append(v2)
              
def print_graph():
    global graph
    global vertices_num

    for vertex in graph:
        for edge in graph[vertex]:
            print(f"{vertex} -> {edge}")

# BFS Start -----------------------------------------------------------#
def BFS(visited , graph , node):
    global queue 
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m , end = ' ')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# BFS End --------------------------------------------------------------#





if __name__ == "__main__":
# A dictionary holds all the Vertices and Edges 
    graph = {}
    vertices_num = 0 

    visited , queue = [],[]

    create_vertex(1)
    create_vertex(2)
    create_vertex(3)
    create_vertex(4)
    create_vertex(5)

    link_vertices(1,2)
    link_vertices(1,3)
    link_vertices(2,3)
    link_vertices(3,4)
    link_vertices(4,1) 

    print_graph()
    BFS(visited , graph , 3)


