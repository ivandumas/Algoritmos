class DFSAdj:

    matrix = []

    def __init__(self, vert, arista):
        self.vert = vert
        self.arista,
        for i in range(vert):
            row =[]
            for j in range(vert):
                row.append(0)
            DFSAdj.matrix.append(row)
    
    def arista(self, inicio, arista):
        DFSAdj.matrix[inicio][arista] = 1
        DFSAdj.matrix[arista][inicio] = 1
    
    def method(self,inicio,flags):
        print(str(inicio)+"-->", end= '')
        flags[inicio] = True
        for i in range(self.vert):
            if(DFSAdj.matrix[inicio][i] == 1 and flags[i] == False):
                self.method(i,flags)

if __name__ == "__main__":
    vertices = 5
    aristas = 5

    grafo = DFSAdj(vertices,aristas)

    grafo.arista(0,1)
    grafo.arista(0,3)
    grafo.arista(1,2)
    grafo.arista(1,4)
    grafo.arista(2,3)

    flags = []
    for i in range(vertices):
        flags.append(False)

    grafo.method(0,flags)
    print()