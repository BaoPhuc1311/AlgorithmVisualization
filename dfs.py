import tkinter as tk
import time
import threading

class DFSVisualization:
    def __init__(self, canvas):
        self.canvas = canvas
        self.graph = {
            'A': (300, 100), 'B': (200, 200), 'C': (400, 200),
            'D': (150, 300), 'E': (250, 300), 'F': (450, 300)
        }
        self.edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]
        self.visited = set()
        self.running = False
        self.paused = False
        self.current_node = None
        self.dfs_thread = None
        self.adjusted_graph = {}

    def draw_graph(self):
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_offset = canvas_width // 2 - 300
        y_offset = canvas_height // 2 - 200 
        
        self.adjusted_graph = {node: (x + x_offset, y + y_offset) for node, (x, y) in self.graph.items()}
        
        for u, v in self.edges:
            x1, y1 = self.adjusted_graph[u]
            x2, y2 = self.adjusted_graph[v]
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        for node, (x, y) in self.adjusted_graph.items():
            self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="lightgray", outline="black", width=2)
            self.canvas.create_text(x, y, text=node, font=("Arial", 14, "bold"))

    def visualize_step(self, node):
        if not self.running or self.paused:
            return
        x, y = self.adjusted_graph[node]
        self.canvas.create_oval(x-25, y-25, x+25, y+25, fill="#27AE60", outline="black", width=2)
        self.canvas.create_text(x, y, text=node, font=("Arial", 14, "bold"), fill="white")
        self.canvas.update()
        time.sleep(1)

    def dfs(self, graph, node):
        if node not in self.visited and self.running:
            self.visited.add(node)
            self.current_node = node
            self.visualize_step(node)
            for neighbor in graph.get(node, []):
                while self.paused:
                    time.sleep(0.1)
                self.dfs(graph, neighbor)

    def start_dfs(self):
        self.running = True
        self.paused = False
        self.visited.clear()
        self.draw_graph()
        
        self.dfs_thread = threading.Thread(target=self.dfs, args=({'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}, 'A'))
        self.dfs_thread.start()

    def pause_dfs(self):
        self.paused = True
    
    def continue_dfs(self):
        if not self.running or self.current_node is None:
            return
        self.paused = False
        self.dfs(self.graph, self.current_node)

    def reset_dfs(self):
        self.running = False
        self.paused = False
        self.current_node = None
        self.draw_graph()
