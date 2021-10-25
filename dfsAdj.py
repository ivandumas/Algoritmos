from pyvis.network import Network

class DFSAdj:

    matrix = []
    nodes = [] #For pyvis

    net = Network()

    def __init__(self, vert, arista):
        self.vert = vert
        self.arista,
        for i in range(vert):
            row =[]
            DFSAdj.nodes.append(i)
            for j in range(vert):
                row.append(0)
            DFSAdj.matrix.append(row)
        DFSAdj.net.add_nodes(DFSAdj.nodes)
    
    def arista(self, inicio, arista):
        DFSAdj.net.add_edge(inicio, arista, weight=.87)
        DFSAdj.matrix[inicio][arista] = 1
        DFSAdj.matrix[arista][inicio] = 1
    
    def method(self,inicio,flags):
        print(str(inicio)+"-->", end= '')
        flags[inicio] = True
        for i in range(self.vert):
            if(DFSAdj.matrix[inicio][i] == 1 and flags[i] == False):
                self.method(i,flags)
    
    def graph(self):
        DFSAdj.net.toggle_physics(True)
        DFSAdj.net.show('mygraph.html')

if __name__ == "__main__":
    vertices = 6
    aristas = 6

    grafo = DFSAdj(vertices,aristas)

    grafo.arista(0,1)
    grafo.arista(0,3)
    grafo.arista(1,2)
    grafo.arista(1,4)
    grafo.arista(2,3)
    grafo.arista(4,5)

    flags = []
    for i in range(vertices):
        flags.append(False)

    grafo.method(0,flags)
    print()
    grafo.graph()
