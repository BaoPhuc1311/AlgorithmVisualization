import tkinter as tk
import time
import threading
from collections import deque

class BFSVisualization:
    def __init__(self, canvas):
        self.canvas = canvas
        self.graph = {
            'A': (300, 100), 'B': (200, 200), 'C': (400, 200),
            'D': (150, 300), 'E': (250, 300), 'F': (450, 300)
        }
        self.edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]
        self.running = False
        self.paused = False
        self.queue = deque()
        self.visited = set()
        self.bfs_thread = None
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

    def bfs(self, graph, start):
        self.queue.append(start)
        self.visited.add(start)
        
        while self.queue and self.running:
            node = self.queue.popleft()
            self.visualize_step(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in self.visited:
                    while self.paused:
                        time.sleep(0.1)
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
    
    def start_bfs(self):
        self.running = True
        self.paused = False
        self.visited.clear()
        self.queue.clear()
        self.draw_graph()
        
        self.bfs_thread = threading.Thread(target=self.bfs, args=({'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}, 'A'))
        self.bfs_thread.start()
    
    def pause_bfs(self):
        self.paused = True
    
    def continue_bfs(self):
        self.paused = False
    
    def reset_bfs(self):
        self.running = False
        self.paused = False
        self.queue.clear()
        self.draw_graph()
