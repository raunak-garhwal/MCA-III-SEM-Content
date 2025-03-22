import tkinter as tk

class WaterJugVisualizer:
    def __init__(self, capacity, goal):
        self.capacity = capacity
        self.goal = goal
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=600, height=350)
        self.canvas.pack()
        self.jug1_x, self.jug2_x = 100, 300
        self.jug_y, self.jug_width, self.jug_height = 50, 60, 200
        self.window.title("Water Jug Problem Visualization")
    
    def update_visualization(self, jug1, jug2, steps):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.jug1_x, self.jug_y, self.jug1_x + self.jug_width, self.jug_y + self.jug_height, outline='black')
        self.canvas.create_rectangle(self.jug2_x, self.jug_y, self.jug2_x + self.jug_width, self.jug_y + self.jug_height, outline='black')
        self.canvas.create_text(self.jug1_x + self.jug_width / 2, self.jug_y + self.jug_height + 10, text="Jug1")
        self.canvas.create_text(self.jug2_x + self.jug_width / 2, self.jug_y + self.jug_height + 10, text="Jug2")
        
        # Draw water levels
        self.canvas.create_rectangle(self.jug1_x, self.jug_y + self.jug_height - (jug1 / self.capacity[0] * self.jug_height),
                                     self.jug1_x + self.jug_width, self.jug_y + self.jug_height, fill="blue")
        self.canvas.create_rectangle(self.jug2_x, self.jug_y + self.jug_height - (jug2 / self.capacity[1] * self.jug_height),
                                     self.jug2_x + self.jug_width, self.jug_y + self.jug_height, fill="blue")
        
        # Add water level text and steps taken
        self.canvas.create_text(self.jug1_x + self.jug_width / 2, self.jug_y + self.jug_height - (jug1 / self.capacity[0] * self.jug_height) - 10, text=f'{jug1}/{self.capacity[0]}')
        self.canvas.create_text(self.jug2_x + self.jug_width / 2, self.jug_y + self.jug_height - (jug2 / self.capacity[1] * self.jug_height) - 10, text=f'{jug2}/{self.capacity[1]}')
        self.canvas.create_text(300, 20, text="Steps: " + " -> ".join(steps), font=("Arial", 10, "bold"))
        self.window.update()

    def run(self, solution_path):
        steps = [f"{x}, {y}" for x, y in solution_path]
        for state in solution_path:
            self.update_visualization(*state, steps)
            self.window.after(2000)  # Delay for visualization
        self.window.mainloop()

def water_jug_bfs(capacity, goal):
    queue, visited = [(0, 0, [])], {(0, 0)}
    visualizer = WaterJugVisualizer(capacity, goal)

    while queue:
        x, y, path = queue.pop(0)
        if x == goal or y == goal:
            visualizer.run(path + [(x, y)])
            return
        next_states = [
            (capacity[0], y), (x, capacity[1]), (0, y), (x, 0), 
            (x - min(x, capacity[1] - y), y + min(x, capacity[1] - y)), 
            (x + min(y, capacity[0] - x), y - min(y, capacity[0] - x))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(x, y)]))
    
    print("No solution found.")

def get_input():
    jug1_capacity = int(input("Enter Jug1 capacity: "))
    jug2_capacity = int(input("Enter Jug2 capacity: "))
    goal = int(input("Enter goal: "))
    water_jug_bfs((jug1_capacity, jug2_capacity), goal)

get_input()
