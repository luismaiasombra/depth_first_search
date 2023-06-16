import random
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
        self.x = random.randint(100, 700)

class Graph:
    def __init__(self):
        self.adjacency_list = []

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
        if pair[0] not in numbers:
            numbers.append(pair[0])
            new_node = Node(pair[0])
            
            if pair[1] not in numbers2:
                numbers2.append(pair[1])
                node2 = Node(pair[1])
                new_node.neighbor.append(node2)
            
            adjacency_list.append(new_node)          
        else:
            #pair0 is in numbers
            for node in adjacency_list:
                if node.number == pair[0]:
                    if pair[1] not in numbers2:
                        node.neighbor.append(Node(pair[1]))
                        numbers2.append(pair[1])
    adjacency_list.sort(key=lambda node: node.number)
    for i in adjacency_list:
        i.neighbor.sort(key=lambda node: node.number)
    return adjacency_list

class Time():
    def __init__(self, value):
        self.value = value

def DFS_VISIT(u, time):
    print("visiting ",u.number)
    #if (u.pi != None):
    #    draw_arrow(canvas,u.x,u.y,u.pi.x,u.pi.y)
    
    time.value = time.value + 1
    u.d = time.value
    u.color = "gray"
    for v in u.neighbor:
        if v.color == "white":
            v.pi = u
            DFS_VISIT(v, time)
    time.value = time.value + 1
    u.f = time.value
    print("completed visiting ",u.number)
    u.color = "black"

def draw_circle(canvas, radius, node):
    x = node.x
    y = node.y
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black')
    canvas.create_text(x, y, text=str(node.number), fill='black')

def DFS(start_node, time):
    for u in start_node.neighbor:
        u.color = "white"
        u.pi = None
    time.value = 0
    for u in start_node.neighbor:
        if u.color == "white":
            DFS_VISIT(u, time)

time = Time(0)
graph = Graph()
numbers = read_numbers("./numbers.txt")
print(numbers)
graph.adjacency_list = create_adjacency_list(numbers)



def create_circles(graph, canvas):
    numbers1 = []
    numbers2 = []
    for i in graph.adjacency_list:
        if i.number not in numbers1:
            numbers1.append(i.number)
            draw_circle(canvas, 30, i)
        for j in i.neighbor:
            if j.number not in numbers2:
                numbers2.append(j.number)
                draw_circle(canvas, 30, j)
import tkinter as tk

def draw_arrow(canvas, x1, y1, x2, y2, fill="blue"):
    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=fill,width=3)



create_circles(graph,canvas)
for i in graph.adjacency_list:
    for j in i.neighbor:
        draw_arrow(canvas,i.x,i.y,j.x,j.y,"black")
DFS(graph.adjacency_list[0], time)


window.mainloop()
