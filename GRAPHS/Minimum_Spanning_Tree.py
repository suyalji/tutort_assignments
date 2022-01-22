def spa_unweighted(source,graph):
    length = len(graph.keys())
    distance = {}
    for key in graph.keys():
        distance[key] = -1
    print(distance)
    distance[source] = 0
    print(distance)


if __name__ ==  "__main__":
    graph = {
             'C' : {'A','F'},
             'A' : {'B','D'},
             'F' : {},
             'D' : {'F'},
             'B' : {'E','D'},
             'E' : {'G'},
             'G' : {'F'}
    }
source = 'C'
spa_unweighted(source,graph)    