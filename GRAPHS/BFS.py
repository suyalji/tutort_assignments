## BFS
def create_vertex(v):
    global graph
    global vertices_num

    if v in graph:
        print(f"The vertex {v} already exists ")
    else:
        graph[v] = []
        vertices_num += 1       

def link_vertices(v1,v2):
    global graph
    if v1 not in graph:
        print(f"The vertex {v1} does not exists")
    elif v2 not in graph:
        print(f"The vertex {v2} does not exists") 
    else:
        graph[v1].append(v2)
               
def print_graph():
    global graph
    for vertex in graph:
        for edge in graph[vertex]:
            print(f"Vertex {vertex} ---> {edge}")

def print_BFS(graph , vertex):
    visited = []
    queue = []
    visited.append(vertex)
    queue.append(vertex)

    while queue:
        m = queue.pop(0)
        print(m , end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)




if __name__ == "__main__":
    graph = {}
    vertices_num = 0 

    create_vertex(0)
    create_vertex(1)
    create_vertex(2)
    create_vertex(3)
    
    link_vertices(0,1)
    link_vertices(0,2)
    link_vertices(1,2)
    link_vertices(2,0)
    link_vertices(2,3)
    link_vertices(3,3)
    
    print(graph)
    print_graph()
    print_BFS(graph, 0)






