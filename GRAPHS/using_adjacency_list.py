def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print(f"Vertex {v} already exists.. ")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []    

def add_edge(v1,v2,e):
    # Add an edge between vertex v1 and v2 with edge weight e
    global graph
    # Check if vertex v1 is a valid vertex 
    if v1 not in graph:
        print(f"Vertex {v1} does not exists")
    elif v2 not in graph:
        print(f"Vertex {v2} does not exists")
    else:
        temp = [v2,e]
        graph[v1].append(temp)

def print_graph():
    global graph 
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex,"->",edges[0],"edge weight: ",edges[1])


if __name__ == "__main__":
    # Global Variables 
    graph = {}
    vertices_no = 0 

    add_vertex(1)
    add_vertex(2)
    add_vertex(3)
    add_vertex(4)

    add_edge(1,2,1)
    add_edge(1,3,1)
    add_edge(2,3,3)
    add_edge(3,4,4)
    add_edge(4,1,5)

    print_graph()

    print("Internal Representation : ", graph)