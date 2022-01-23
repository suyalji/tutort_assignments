# ---------------------------------------------------------------------#
# Problem : Find number of Islands in a graph                          #
# Counting the number of Connected components in an undirected graph   #
# Kind of 4-way BFS BackTracking                                       # 
# ---------------------------------------------------------------------#

def num_islands(graph):
    rows  = len(graph)
    cols  = len(graph[0])
    
    if rows == 0:
        return 

    count = 0 

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1:
                markCurrentIsland(graph, i, j, rows, cols)
                # The count will always increment when an Island is completed  
                count += 1
    return count 

def markCurrentIsland(graph,i,j,rows,cols):
    if i<0 or i>= rows or j < 0 or j >= cols or graph[i][j] != 1:
        return 
    graph[i][j] = 2

    markCurrentIsland(graph, i+1, j, rows, cols)
    markCurrentIsland(graph, i, j+1, rows, cols)
    markCurrentIsland(graph, i-1, j, rows, cols)
    markCurrentIsland(graph, i, j-1, rows, cols)


if __name__ == "__main__":
    graph  =[
                [[1,1,0,1],[1,1,0,0],[0,1,0,1],[0,0,0,1]],
                [[1,1,1,1],[1,1,0,1],[0,0,0,1],[0,0,0,1]],
                [[1,0],[0,1]],
                [[1,1,0,1]]
            ]
            
    for matrix in graph:        
        print(f"Number of Islands in the graph : {num_islands(matrix)}")   

# COMPLETED              