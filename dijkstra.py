from queue import PriorityQueue

metro = ['El Rosario','Instituto del Petroleo','Deportivo 18 de Marzo','Martin Carrera','La Raza', 
        'Consulado','Tacuba','Oceania','Guerrero','Garibaldi','Hidalgo','Bellas Artes', 'Morelos',
        'San Lazaro', 'Balderas','Salto del Agua','Pino Suarez','Candelaria','Tacubaya','Pantitlan',
        'Centro Medico', 'Chabacano','Jamaica','Santa Anita','Mixcoac','Zapata','Ermita','Atlalinco'] 

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def addEdge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

g = Graph(28)
g.addEdge(0, 1, 5)
g.addEdge(0, 6, 3)
g.addEdge(1, 2, 1)
g.addEdge(1, 4, 1)
g.addEdge(2, 3, 1)
g.addEdge(3, 5, 2)
g.addEdge(4, 2, 1)
g.addEdge(4, 5, 2)
g.addEdge(4, 8, 1)
g.addEdge(5, 7, 2)
g.addEdge(5, 12, 1)
g.addEdge(6, 10, 6)
g.addEdge(6, 18, 4)
g.addEdge(7, 13, 2)
g.addEdge(7, 19, 2)
g.addEdge(8, 9, 0)
g.addEdge(8, 10, 0)
g.addEdge(9, 11, 0)
g.addEdge(9, 12, 2)
g.addEdge(10, 11, 0)
g.addEdge(10, 14, 1)
g.addEdge(11, 15, 1)
g.addEdge(11, 16, 2)
g.addEdge(12, 13, 0)
g.addEdge(12, 17, 0)
g.addEdge(13, 17, 0)
g.addEdge(13, 19, 5)
g.addEdge(14, 18, 5)
g.addEdge(14, 15, 0)
g.addEdge(14, 20, 2)
g.addEdge(15, 16, 1)
g.addEdge(15, 21, 2)
g.addEdge(16, 17, 0)
g.addEdge(16, 21, 1)
g.addEdge(17, 22, 1)
g.addEdge(18, 20, 2)
g.addEdge(18, 24, 2)
g.addEdge(19, 22, 4)
g.addEdge(20, 21, 1)
g.addEdge(20, 25, 3)
g.addEdge(21, 22, 0)
g.addEdge(21, 23, 1)
g.addEdge(21, 26, 5)
g.addEdge(22, 23, 0)
g.addEdge(23, 27, 5)
g.addEdge(24, 25, 2)
g.addEdge(25, 26, 2)
g.addEdge(26, 27, 1)



print ("BFT:")
D = g.dijkstra(0)

for vertex in range(len(D)):
    print(f"Distance from El Rosario to {metro[vertex]}, is {D[vertex]}")