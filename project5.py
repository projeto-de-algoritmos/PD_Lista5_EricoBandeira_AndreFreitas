from collections import defaultdict 
import os

class Grafo: 
  
    def __init__(self, vertices): 
        self.V = vertices  
        self.Grafo = [] 
   
    def adicionarVertice(self, u, v, w): 
        self.Grafo.append([u, v, w]) 


    def printarVetor(self, dist): 
        print("Distância de cada vertice é:") 
        for i in range(self.V): 
            print("% d \t\t % d" % (i, dist[i])) 
      
      
    def BellmanFord(self, src): 
        dist = [float("Inf")] * self.V 
        dist[src] = 0 
         
        for i in range(self.V - 1): 
            for u, v, w in self.Grafo: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
       
        for u, v, w in self.Grafo: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print ("Grafo contem um ciclo de distancias negativa")
                        return
                          
        
        self.printarVetor(dist) 

cond = True
qntVertice =int(input("Digite aqui quantos vértices tem o seu grafo:\n"))
os.system('cls' if os.name == 'nt' else 'clear')


g = Grafo(qntVertice) 


while(cond):
    print("informe agora o vertice inicial, o vértice final e o peso da aresta!\n")
    print("Se não existir mais arestas escreva 'c' para calcular Bellman-Ford")

    verticeInicial = input()

    if(verticeInicial == 'c'):
        cond = False 
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    verticeFinal = input()
    pesoAresta = input()
    g.adicionarVertice(int(verticeInicial), int(verticeFinal), int(pesoAresta)) 
    os.system('cls' if os.name == 'nt' else 'clear')



os.system('cls' if os.name == 'nt' else 'clear')
verticeReferencia = int(input("Informe agora o vertice de referência:"))

g.BellmanFord(verticeReferencia)