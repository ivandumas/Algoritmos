from collections import defaultdict

class Graph:
    metro = ['El Rosario','Instituto del Petroleo','Tacuba','Hidalgo','Tacubaya', 'Deportivo 18 de Marzo','Centro Medico','Mixcoac','Balderas','Bellas Artes','Guerrero','Martin Carrera','Zapata','Chabacano',
    'Salto del Agua','Garibaldi','La Raza', 'Pino Suarez','Consulado','Candelaria', 'Ermita','Santa Anita','Oceania','Morelos',
    'San Lazaro','Jamaica','Atlalilco', 'Pantitlan']

    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        #agregar un Edge al grafo
        for val in v:
            self.graph[u].append(val)
 
    def BFS(self, s):
        #realizar el BFS
        d = []
        for i in range(100):
            d.append(0)
            
        d[s]=0
        queue = []
 
        visited = [False] * (max(self.graph) + 1)
 
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")

            for v in self.graph[s]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True
                    d[v]= d[s]+1

        print("\nNodo inicial: El Rosario")
        for i in range(28):
            print(f"Desde el Rosario hasta {self.metro[i]} es {d[i]}")


g = Graph()
g.addEdge(0, [1,2])
g.addEdge(1, [14,15])
g.addEdge(2, [3,4])
g.addEdge(3, [11,12])
g.addEdge(4, [5,6,9])
g.addEdge(5, [8,9])
g.addEdge(6, [7])
g.addEdge(7, [25])
g.addEdge(8, [10,21,25,26])
g.addEdge(9, [3,10])
g.addEdge(11, [10,21])
g.addEdge(12, [13,14])
g.addEdge(13, [11])
g.addEdge(14, [15,17])
g.addEdge(15, [16])
g.addEdge(17, [16,18,19])
g.addEdge(18, [23])
g.addEdge(19, [13,20])
g.addEdge(20, [18,23])
g.addEdge(21, [10,22])
g.addEdge(22, [19,20])
g.addEdge(23, [24])
g.addEdge(24, [8,22])
g.addEdge(25, [27])
g.addEdge(26, [24,27])
 
print ("BFT:")
g.BFS(0)