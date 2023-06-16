#primeira linha: n
import random as random
import tkinter as tk
window = tk.Tk()
window.geometry("800x800")
canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()
class Node:
    def __init__(self, number):
        self.number = number
        self.f = None
        self.d = None
        self.neighbor = []
        self.pi = None
        self.color = "white"
        self.y = random.randint(100, 700)
        self.x = random.randint(100,700)
        
    #a lista de adjacencia é uma lista de nós
    #por tanto


class Graph:
    
    adjacency_list = []
    def __init__(self):
        self.vertexes = []
        self.main_numbers = []
        self.vertexes = set()
    
    



def read_numbers(file_path):
    result = []

    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 2:
                num_array = [int(numbers[0]), int(numbers[1])]
                result.append(num_array)

    return result



def create_adjacency_list(array):
    adjacency_list = []
    numbers = []
    numbers2 = []
    for pair in array:
        #vamos fazer v = u para acabar com os repetidos
        if pair[0] not in numbers:
            numbers.append(pair[0])
            new_node = Node(pair[0])
            
            if pair[1] not in numbers2:
                numbers2.append(pair[1])
                node2 = Node(pair[1])
                new_node.neighbor.append(node2)
                
            else:
                #primeiro digito nao está no numero, e o segundo está
                pass
            #a gente adiciona o no principal so depois
            adjacency_list.append(new_node)          
            
        else:
            #pair[0] is in numbers
            for node in adjacency_list:
                if node.number == pair[0]:
                    if pair[1] not in numbers2:
                        node.neighbor.append(Node(pair[1]))
                        numbers2.append(pair[1],)
    return adjacency_list
    adjacency_list.sort(key=lambda node: node.number)
    for i in adjacency_list:
        i.neighbor.sort(key=lambda node: node.number)
    return adjacency_list
    
class Time():
    def __init__(self,value):
        self.value = value



def DFS_VISIT(u,time):
    ip = input("Press anything to proceed")
    time.value = time.value + 1
    u.d = time.value
    u.color = "gray"
    for v in u.neighbor:
        if v.color == "white":
            v.pi = u

            DFS_VISIT(v,time)
    time.value = time.value + 1
    u.f = time.value
    u.color = "black"

def create_circle(canvas, radius, node):
    # Generate random coordinates for the circle
    x = node.x
    y =node.y

    # Draw the circle
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black')

    # Place the number inside the circle
    canvas.create_text(x, y, text=str(node.number), fill='black')
def DFS(start_node,time):
    for u in start_node.neighbor:
        u.color="white"
        u.pi = None
    time.value = 0
    for u in start_node.neighbor:
        if u.color=="white":
            DFS_VISIT(u,time)
time = Time(0)
graph = Graph()
numbers = read_numbers("./numbers.txt")
graph.adjacency_list = create_adjacency_list(numbers)
for i in graph.adjacency_list:
    print(i.number)

def draw_line(canvas, node1, node2):
    canvas.create_line(node1.x, node1.y, node2.x, node2.y, fill='white')

# Example usage:




def create_edges(graph,canvas):
    for i in graph.adjacency_list:
        create_circle(canvas,30,i)
        for j in graph.adjacency_list:
            create_circle(canvas,30,j)
            draw_line(canvas,i,j)

create_edges(graph,window)
DFS(graph.adjacency_list[0],time)



#for i in adj_list:
#    print(i.number,":",end="")
#    for j in i.neighbor:
#        print(j.number,"->",end='')
#    print("")





 #populates vector attribute

