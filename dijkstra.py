import tkinter as tk
import heapq
import time
import threading

class DijkstraVisualization:
    def __init__(self, canvas):
        self.canvas = canvas
        self.graph = {
            'A': {'B': 4, 'D': 2},
            'B': {'A': 4, 'D': 5, 'E': 10},
            'C': {'E': 3, 'F': 7},
            'D': {'A': 2, 'B': 5, 'E': 2, 'F': 6},
            'E': {'B': 10, 'C': 3, 'D': 2, 'F': 8},
            'F': {'C': 7, 'D': 6, 'E': 8}
        }
        self.positions = {
            'A': (150, 150), 'B': (250, 100), 'C': (500, 150),
            'D': (250, 200), 'E': (400, 100), 'F': (450, 200)
        }
        self.running = False
        self.paused = False
        self.adjusted_positions = {}
        self.current_node = None
        self.priority_queue = []
        self.distances = {}

    def draw_graph(self):
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_offset = canvas_width // 2 - 325
        y_offset = canvas_height // 2 - 150 
        
        self.adjusted_positions = {node: (x + x_offset, y + y_offset) for node, (x, y) in self.positions.items()}
        
        for u, neighbors in self.graph.items():
            for v, weight in neighbors.items():
                x1, y1 = self.adjusted_positions[u]
                x2, y2 = self.adjusted_positions[v]
                self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2, smooth=True)
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2 - 10, text=str(weight), font=("Arial", 10), fill="red")

        for node, (x, y) in self.adjusted_positions.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightgray", outline="black", width=2)
            self.canvas.create_text(x, y, text=node, font=("Arial", 12, "bold"))

    def visualize_step(self, node, color):
        x, y = self.adjusted_positions[node]
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black", width=2)
        self.canvas.create_text(x, y, text=node, font=("Arial", 12, "bold"), fill="white")
        self.canvas.update()
        time.sleep(1)

    def dijkstra(self, start):
        self.running = True
        self.paused = False
        self.distances = {node: float('inf') for node in self.graph}
        self.distances[start] = 0
        self.priority_queue = [(0, start)]
        
        while self.priority_queue and self.running:
            while self.paused:
                time.sleep(0.1)
            
            current_distance, self.current_node = heapq.heappop(self.priority_queue)
            self.visualize_step(self.current_node, "#27AE60")
            
            for neighbor, weight in self.graph[self.current_node].items():
                distance = current_distance + weight
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    heapq.heappush(self.priority_queue, (distance, neighbor))
    
    def start_dijkstra(self):
        self.draw_graph()
        threading.Thread(target=self.dijkstra, args=("A",)).start()

    def pause_dijkstra(self):
        self.paused = True
    
    def continue_dijkstra(self):
        self.paused = False
    
    def reset_dijkstra(self):
        self.running = False
        self.paused = False
        self.draw_graph()
