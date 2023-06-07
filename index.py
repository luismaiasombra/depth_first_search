import sys
import random
from tkinter import Tk, Button
import time

# Definindo a classe do grafo
import tkinter as tk;
class Grafo:
    def __init__(self): #o objeto grafo tem vertices e arestas
        self.vertices = {}
        self.arestas = {} #aqui temos um dicionário vazio
    #a chave chave é vértice e o valor é uma lista vazia
    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = []
        self.arestas[vertice] = {}
    #a chave é vertice e o valor é um dicionário vazio
    def adicionar_aresta(self, origem, destino):
        self.vertices[origem].append(destino) #adiciona um destino, sendo que partiu do vertice origem
        self.arestas[origem][destino] = None

    def grau_saida(self, vertice):
        return len(self.vertices[vertice])

    def get_vertices(self):
        return self.vertices

    def get_arestas(self):
        return self.arestas

# Função para ler o grafo a partir do arquivo
def ler_grafo(arquivo):
    grafo = Grafo()

    with open(arquivo, 'r') as file:
        linhas = file.readlines()

        # Obtendo o número de vértices e arestas
        header = linhas[0].split()
        num_vertices = int(header[0])
        num_arestas = int(header[1])

        # Adicionando os vértices ao grafo
        for i in range(1, num_vertices+1):
            grafo.adicionar_vertice(str(i))

        # Adicionando as arestas ao grafo
        for i in range(1, num_arestas+1):
            aresta = linhas[i].split()
            origem = aresta[0]
            destino = aresta[1]
            grafo.adicionar_aresta(origem, destino)

    return grafo

# Função DFS modificada para imprimir o vetor d, vetor f e o tipo de aresta
def dfs(grafo, vertice):
    d = {}
    f = {}
    tempo = 0

    # Função auxiliar para realizar a DFS a partir de um vértice
    def dfs_visit(v):
        nonlocal tempo
        tempo += 1
        d[v] = tempo

        for vizinho in grafo.get_vertices()[v]:
            if vizinho not in d:
                grafo.get_arestas()[v][vizinho] = "Aresta de Árvore"
                #aqui é onde vamos fazer a bolinha acender5
                dfs_visit(vizinho)
            elif vizinho not in f:
                grafo.get_arestas()[v][vizinho] = "Aresta de Retorno"
            else:
                if d[v] < d[vizinho]:
                    grafo.get_arestas()[v][vizinho] = "Aresta de Avanço"
                else:
                    grafo.get_arestas()[v][vizinho] = "Aresta de Cruzamento"

        tempo += 1
        f[v] = tempo

    # Obtendo o vértice com o maior grau de saída
    vertices = grafo.get_vertices()
    vertices_ordenados = sorted(vertices.keys(), key=lambda v: grafo.grau_saida(v), reverse=True)
    maior_grau_saida = grafo.grau_saida(vertices_ordenados[0])

    for v in vertices_ordenados:
        if grafo.grau_saida(v) == maior_grau_saida:
            dfs_visit(v)
            break
    
    # Imprimindo o vetor d, vetor f e o tipo de aresta
    print("Vetor d:", d)
    print("Vetor f:", f)
    print("Tipos de arestas:")
    for origem in grafo.get_arestas():
        for destino, tipo in grafo.get_arestas()[origem].items():
            print(f"{origem} -> {destino}: {tipo}")
    return [f,d]
# Verificando se foi fornecido o arquivo como argumento do terminal
if len(sys.argv) < 2:
    print("É necessário fornecer o nome do arquivo como argumento do terminal.")
    print("Exemplo de uso: python dfs.py grafo.txt")
    sys.exit()

# Obtendo o nome do arquivo a partir dos argumentos do terminal
nome_arquivo = sys.argv[1]

# Executando o algoritmo DFS no grafo carregado do arquivo fornecido
grafo = ler_grafo(nome_arquivo)


def populate_grid(dictionary):
    pass
[f,d]=dfs(grafo, '1')
print("f = ", f)
print("d = ",d)
############################################
window = tk.Tk()
window.title("Hello World!")

def handle_button_press(event):
    window.destroy()
###############################################
GRID_SIZE = 10
CELL_SIZE = 50
canvas = tk.Canvas(window, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE)
canvas.circle_pos=[]
canvas.numbers = []
def draw_circle(x, y, radius, color,number):
    if x!=None and y!= None:
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)
        canvas.create_text(x, y, text=str(number), font=('Arial', 10), fill='blue')
        canvas.circle_pos.append([number,x,y])
def draw_aresta(number1,number2,line_color):
    if (get_circle_coords(number1)!=None and get_circle_coords(number2)!=None):
        x1,x2 =get_circle_coords(number1)
        x3,x4 = get_circle_coords(number2)
        canvas.create_line(x1,x2,x3,x4,fill=line_color)

def get_circle_coords(number):
    for i in canvas.circle_pos:
        if i[0] == number:
            return i[1],i[2]
    return None
    #imlementar função que guarda o x e o y para criar arestas
#vamos popular o grid com as chaves de f

###############################################
button = tk.Button(text = "Close")
button.bind("<Button-1>", handle_button_press)
button.pack()
canvas.pack()
###############################################

#criando os círculos

for key in grafo.get_vertices():
    x = random.randint(100,400)
    y = random.randint(100,400)
    draw_circle(x,y,15,"white",int(key))

arestas = grafo.get_arestas()
arestas_formatadas = []



for i in arestas:
    for key in arestas[i]:
        print(i,key)
        arestas_formatadas.append([i,key])

print("arestas formatadas: ",arestas_formatadas)
#criando as arestas
for array in arestas_formatadas:
    number1 = array[0]
    number2 = array[1]
    print("array:",number1,number2)
    draw_aresta(int(number1),int(number2),"black")

# Create the grid of circles

tempo = 1


if max(f.values()) > max(d.values()):
    maximum = max(f.values())
else:
    maximum = max(d.values())
tempo = 1
print("maximum: ",maximum)


while tempo<maximum:
    x = input()
    for key, value in d.items():
        if value ==tempo:
            x,y = get_circle_coords(int(value))
            draw_circle(x,y,15,"gray",int(value))
    for key, value in f.items():
        if value ==tempo:
            x,y = get_circle_coords(int(value))
            draw_circle(x,y,15,"black",int(value))    
    tempo+=1
 
    
window.title("Grafos")
print("f:",f)
print("d:",d)

#podemos fazer um vetor intercalado, vertice 6fica preto em t =4.
window.mainloop()