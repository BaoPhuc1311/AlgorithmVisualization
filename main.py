import tkinter as tk
from tkinter import ttk
from dijkstra import DijkstraVisualization

class AlgorithmVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualization")
        self.root.state("zoomed")

        self.dark_mode = True
        self.set_theme()

        self.title_label = tk.Label(root, text="Algorithm Visualization", font=("Arial", 18, "bold"), bg=self.bg_color, fg=self.text_color)
        self.title_label.pack(pady=10)

        self.algorithm_label = tk.Label(root, text="Select Algorithm:", font=("Arial", 12), bg=self.bg_color, fg=self.text_color)
        self.algorithm_label.pack(pady=5)

        self.algorithms = ["Dijkstra"]
        self.algorithm_var = tk.StringVar()

        self.algorithm_combobox = ttk.Combobox(root, textvariable=self.algorithm_var, values=self.algorithms, state="readonly", font=("Arial", 12), width=20, justify="center")
        self.algorithm_combobox.set("Scroll")
        self.algorithm_combobox.pack(pady=5)

        self.algorithm_combobox.bind("<<ComboboxSelected>>", self.set_algorithm)

        self.button_frame = tk.Frame(root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", font=("Arial", 12), bg=self.button_bg, fg=self.button_fg, width=10, relief="raised", bd=3, activebackground=self.button_hover, command=self.start_visualization)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(self.button_frame, text="Pause", font=("Arial", 12), bg=self.button_bg, fg=self.button_fg, width=10, relief="raised", bd=3, activebackground=self.button_hover, command=self.toggle_pause)
        self.pause_button.grid(row=0, column=1, padx=5)
        self.is_paused = False

        self.reset_button = tk.Button(self.button_frame, text="Reset", font=("Arial", 12), bg=self.button_bg, fg=self.button_fg, width=10, relief="raised", bd=3, activebackground=self.button_hover, command=self.reset_visualization)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.toggle_theme_button = tk.Button(root, text="Toggle Theme", font=("Arial", 12), bg="#F39C12", fg="white", width=15, relief="raised", bd=3, command=self.toggle_theme)
        self.toggle_theme_button.pack(pady=10)

        self.canvas_frame = tk.Frame(root, bg=self.frame_bg, bd=3, relief="ridge")
        self.canvas_frame.pack(pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg=self.canvas_bg)
        self.canvas.pack(fill="both", expand=True)

        self.dijkstra_vis = None

    def set_theme(self):
        if self.dark_mode:
            self.bg_color = "#2C3E50"
            self.text_color = "#ECF0F1"
            self.button_bg = "#3498DB"
            self.button_fg = "#ffffff"
            self.button_hover = "#5DADE2"
            self.frame_bg = "#34495E"
            self.canvas_bg = "#1C2833"
        else:
            self.bg_color = "#F5F6FA"
            self.text_color = "#2C3E50"
            self.button_bg = "#007AFF"
            self.button_fg = "#ffffff"
            self.button_hover = "#74b9ff"
            self.frame_bg = "#D6DBDF"
            self.canvas_bg = "#FBFCFC"
        self.root.configure(bg=self.bg_color)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
        self.title_label.config(bg=self.bg_color, fg=self.text_color)
        self.algorithm_label.config(bg=self.bg_color, fg=self.text_color)
        self.button_frame.config(bg=self.bg_color)
        self.canvas_frame.config(bg=self.frame_bg)
        self.canvas.config(bg=self.canvas_bg)
        self.start_button.config(bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)
        self.pause_button.config(bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)
        self.reset_button.config(bg=self.button_bg, fg=self.button_fg, activebackground=self.button_hover)

    def set_algorithm(self, event):
        algo = self.algorithm_var.get()
        self.show_visualization(None)

    def show_visualization(self, event):
        algo = self.algorithm_var.get()
        if algo == "Dijkstra":
            self.canvas.delete("all")
            self.dijkstra_vis = DijkstraVisualization(self.canvas)
            self.dijkstra_vis.draw_graph()

    def start_visualization(self):
        if self.dijkstra_vis:
            self.dijkstra_vis.start_dijkstra()

    def toggle_pause(self):
        if self.dijkstra_vis:
            self.is_paused = not self.is_paused
            if self.is_paused:
                self.pause_button.config(text="Continue")
                self.dijkstra_vis.pause_dijkstra()
            else:
                self.pause_button.config(text="Pause")
                self.dijkstra_vis.continue_dijkstra()

    def reset_visualization(self):
        if self.dijkstra_vis:
            self.is_paused = False
            self.pause_button.config(text="Pause")
            self.dijkstra_vis.reset_dijkstra()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizationApp(root)
    root.mainloop()
