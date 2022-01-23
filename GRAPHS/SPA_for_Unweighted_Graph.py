def spa_unweighted(source,graph):
    length = len(graph.keys())
    distance = {}
    for key in graph.keys():
        distance[key] = -1
    distance[source] = 0
        
    queue = []
    queue.append(source)
        
    while(len(queue) > 0):
        curr = queue.pop(0)
        curr_node = graph[curr]
        
        for i in graph[curr]:
            if i not in queue:
                queue.append(i)
    
        for i in curr_node:
            if distance[i] == -1:
                distance[i] = distance[curr] + 1
    print(distance)        
        
if __name__ ==  "__main__":
    graph = {
             'C' : ['A','F'],
             'A' : ['B','D'],
             'F' : [],
             'D' : ['F'],
             'B' : ['E','D'],
             'E' : ['G'],
             'G' : ['F']
    }
   
source = 'C'
spa_unweighted(source,graph)    