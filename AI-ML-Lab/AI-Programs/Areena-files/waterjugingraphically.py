import tkinter as tk
from tkinter import messagebox
from collections import deque

# Functions for state transitions (same as before)
def fill_jug(x, y, jug_capacity, jug2_capacity):
    if x < jug_capacity:
        return (jug_capacity, y)
    return None

def fill_jug2(x, y, jug_capacity, jug2_capacity):
    if y < jug2_capacity:
        return (x, jug2_capacity)
    return None

def pour_from_jug1_to_jug2(x, y, jug_capacity, jug2_capacity):
    if x > 0 and y < jug2_capacity:
        transfer_amount = min(x, jug2_capacity - y)
        return (x - transfer_amount, y + transfer_amount)
    return None

def pour_from_jug2_to_jug1(x, y, jug_capacity, jug2_capacity):
    if y > 0 and x < jug_capacity:
        transfer_amount = min(y, jug_capacity - x)
        return (x + transfer_amount, y - transfer_amount)
    return None

def empty_jug1(x, y, jug_capacity, jug2_capacity):
    if x > 0:
        return (0, y)
    return None

def empty_jug2(x, y, jug_capacity, jug2_capacity):
    if y > 0:
        return (x, 0)
    return None

def pour_jug2_into_jug1_until_full(x, y, jug_capacity, jug2_capacity):
    if x + y >= jug_capacity and y > 0:
        transfer_amount = jug_capacity - x
        return (jug_capacity, y - transfer_amount)
    return None

def pour_jug1_into_jug2_until_full(x, y, jug_capacity, jug2_capacity):
    if x + y >= jug2_capacity and x > 0:
        transfer_amount = jug2_capacity - y
        return (x - transfer_amount, jug2_capacity)
    return None

def pour_all_from_jug2_to_jug1(x, y, jug_capacity, jug2_capacity):
    if x + y <= jug_capacity and y > 0:
        return (x + y, 0)
    return None

def pour_all_from_jug1_to_jug2(x, y, jug_capacity, jug2_capacity):
    if x + y <= jug2_capacity and x > 0:
        return (0, x + y)
    return None

def get_possible_actions(x, y, jug_capacity, jug2_capacity):
    actions = [
        fill_jug,
        fill_jug2,
        pour_from_jug1_to_jug2,
        pour_from_jug2_to_jug1,
        empty_jug1,
        empty_jug2,
        pour_jug2_into_jug1_until_full,
        pour_jug1_into_jug2_until_full,
        pour_all_from_jug2_to_jug1,
        pour_all_from_jug1_to_jug2
    ]
    
    valid_actions = []
    for action in actions:
        new_state = action(x, y, jug_capacity, jug2_capacity)
        if new_state:
            valid_actions.append(new_state)
    return valid_actions

def bfs(initial_state, goal_state, jug_capacity, jug2_capacity):
    queue = deque([(initial_state, [])])  
    
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        x, y = current_state
        
        if current_state == goal_state:
            return path
        
        valid_actions = get_possible_actions(x, y, jug_capacity, jug2_capacity)
        for next_state in valid_actions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None  

# GUI class to interact with the user
class JugSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jug Problem Solver")
        
        # Input fields for jug capacities and initial/goal states
        self.jug1_capacity_label = tk.Label(root, text="Capacity of Jug 1:")
        self.jug1_capacity_label.grid(row=0, column=0)
        self.jug1_capacity_entry = tk.Entry(root)
        self.jug1_capacity_entry.grid(row=0, column=1)
        
        self.jug2_capacity_label = tk.Label(root, text="Capacity of Jug 2:")
        self.jug2_capacity_label.grid(row=1, column=0)
        self.jug2_capacity_entry = tk.Entry(root)
        self.jug2_capacity_entry.grid(row=1, column=1)
        
        self.initial_x_label = tk.Label(root, text="Initial amount in Jug 1:")
        self.initial_x_label.grid(row=2, column=0)
        self.initial_x_entry = tk.Entry(root)
        self.initial_x_entry.grid(row=2, column=1)
        
        self.initial_y_label = tk.Label(root, text="Initial amount in Jug 2:")
        self.initial_y_label.grid(row=3, column=0)
        self.initial_y_entry = tk.Entry(root)
        self.initial_y_entry.grid(row=3, column=1)
        
        self.goal_x_label = tk.Label(root, text="Goal amount in Jug 1:")
        self.goal_x_label.grid(row=4, column=0)
        self.goal_x_entry = tk.Entry(root)
        self.goal_x_entry.grid(row=4, column=1)
        
        self.goal_y_label = tk.Label(root, text="Goal amount in Jug 2:")
        self.goal_y_label.grid(row=5, column=0)
        self.goal_y_entry = tk.Entry(root)
        self.goal_y_entry.grid(row=5, column=1)
        
        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.grid(row=6, column=0, columnspan=2)
        
        # Canvas for showing jugs
        self.canvas = tk.Canvas(root, width=400, height=200)
        self.canvas.grid(row=7, column=0, columnspan=2)
        
        self.path = []  # Stores the path of jug states
        self.step = 0   # Step number for BFS path

    def start(self):
        # Get user inputs
        jug_capacity = int(self.jug1_capacity_entry.get())
        jug2_capacity = int(self.jug2_capacity_entry.get())
        initial_x = int(self.initial_x_entry.get())
        initial_y = int(self.initial_y_entry.get())
        goal_x = int(self.goal_x_entry.get())
        goal_y = int(self.goal_y_entry.get())
        
        initial_state = (initial_x, initial_y)
        goal_state = (goal_x, goal_y)
        
        # Solve the problem using BFS
        self.path = bfs(initial_state, goal_state, jug_capacity, jug2_capacity)
        
        if self.path:
            self.display_state(self.path[0])  # Show the initial state
            self.step = 1  # Start with the first state in the path
        else:
            messagebox.showinfo("No Solution", "No solution found.")

    def display_state(self, state):
        x, y = state
        self.canvas.delete("all")  # Clear previous state
        # Display Jug 1 (left) and Jug 2 (right)
        jug1_height = 200 * (x / int(self.jug1_capacity_entry.get()))
        jug2_height = 200 * (y / int(self.jug2_capacity_entry.get()))
        self.canvas.create_rectangle(50, 200 - jug1_height, 150, 200, fill="blue")
        self.canvas.create_rectangle(250, 200 - jug2_height, 350, 200, fill="green")
        self.canvas.create_text(100, 210, text=f"Jug 1: {x}L")
        self.canvas.create_text(300, 210, text=f"Jug 2: {y}L")
        
        if self.step < len(self.path):
            self.root.after(1000, self.display_next_step)  # Show next step after 1 second

    def display_next_step(self):
        if self.step < len(self.path):
            self.display_state(self.path[self.step])
            self.step += 1
        else:
            messagebox.showinfo("Goal Reached", "Goal state reached!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = JugSolverApp(root)
    root.mainloop()
