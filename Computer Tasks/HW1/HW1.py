#!/usr/bin/env python
# coding: utf-8

# # *Assignment 1. Systematic state space search*
# 
# ## *Submitted by Amit Ben Zaken*

# Firstly, we'll implement load_maze to load the inputs from file, and include other helper function for our algorithms.

# In[1]:


import random
import time
from IPython.display import clear_output
from collections import deque
from queue import PriorityQueue
import os


def load_maze(filename):
    with open(filename, "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
    
    maze = []
    start = None
    end = None

    for i, line in enumerate(lines):
        if line.startswith("start"):
            _, coords = line.split(" ", 1)
            start = tuple(map(int, coords.split(",")))
        elif line.lower().startswith("end"):
            _, coords = line.split(" ", 1)
            end = tuple(map(int, coords.split(",")))
        else:
            row = []
            for char in line:
                if char == " ":
                    row.append(-1)
                elif char == "X":
                    row.append(0)
                else:
                    raise ValueError("Invalid character in maze")
            maze.append(row)
    
    start = (start[1], start[0])
    end = (end[1], end[0])
    return maze, start, end

# Function to print the maze with explored nodes and final path
def print_maze_with_path(maze, explored, path, start, end):
    display = [[char for char in row] for row in convert_maze_to_chars(maze)]

    for x, y in explored:
        if (x, y) not in (start, end):
            display[x][y] = "#"

    for x, y in path:
        if (x, y) not in (start, end):
            display[x][y] = "o"

    display[start[0]][start[1]] = "S"
    display[end[0]][end[1]] = "E"

    print("\n".join("".join(row) for row in display))
    print("--------------")

# Convert maze from numbers to characters
def convert_maze_to_chars(maze):
    char_maze = []
    for row in maze:
        char_maze.append(["X" if cell == 0 else " " for cell in row])
    return char_maze

# Function to reconstruct the path
def reconstruct_path(prev, goal):
    x = goal
    path = []
    while x in prev:
        path.append(x)
        x = prev[x]
    path.append(x)
    return path[::-1]

# Get valid neighbors
def get_neighbors(maze, position):
    x, y = position
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 0:
            neighbors.append((nx, ny))

    return neighbors

# We will use Manhattan distance heuristic 
def h(y, end):
    return abs(y[0] - end[0]) + abs(y[1] - end[1]) 


# 1. Random search

# In[2]:


def random_search(maze, start, end):
    
    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        raise ValueError("Start and end positions must be valid")
    
    open_set = {start}
    closed_set = set()
    prev = {}

    while open_set:
        x = random.choice(list(open_set))

        if x == end:
            path = reconstruct_path(prev, x)
            print_maze_with_path(maze, closed_set, path, start, end)
            print("S Start\nE End\n# Opened node\no Path\nX Wall\nspace Fresh node\n--------------")
            print(f"Nodes expanded: {len(closed_set)}")
            print(f"Path length: {len(path) - 1}")
            return path

        for y in get_neighbors(maze, x):
            if y not in open_set and y not in closed_set:
                open_set.add(y)
                prev[y] = x

        open_set.remove(x)
        closed_set.add(x)
        
        print_maze_with_path(maze, closed_set, [], start, end)
        time.sleep(0.3)
        clear_output(wait=True)
        os.system("cls")
        
    print("No path found.")
    return None


# 2. DFS

# In[3]:


def dfs(maze, start, end):
    open_stack = [start]
    closed_set = set()
    prev = {}

    while open_stack:
        x = open_stack.pop()

        if x == end:
            path = reconstruct_path(prev, x)
            print_maze_with_path(maze, closed_set, path, start, end)
            print("S Start\nE End\n# Opened node\no Path\nX Wall\nspace Fresh node\n--------------")
            print(f"Nodes expanded: {len(closed_set)}")
            print(f"Path length: {len(path) - 1}")
            return path

        for y in get_neighbors(maze, x):
            if y not in closed_set and y not in open_stack:
                open_stack.append(y)
                prev[y] = x

        closed_set.add(x)

        print_maze_with_path(maze, closed_set, [], start, end)
        time.sleep(0.3)
        clear_output(wait=True)
        os.system("cls")

    print("No path found.")
    return None


# 3. BFS

# In[4]:


def bfs(maze, start, end):
    open_queue = deque([start])
    closed_set = set()
    prev = {}

    while open_queue:
        x = open_queue.popleft()

        if x == end:
            path = reconstruct_path(prev, x)
            print_maze_with_path(maze, closed_set, path, start, end)
            print("S Start\nE End\n# Opened node\no Path\nX Wall\nspace Fresh node\n--------------")
            print(f"Nodes expanded: {len(closed_set)}")
            print(f"Path length: {len(path) - 1}")
            return path


        for y in get_neighbors(maze, x):
            if y not in closed_set and y not in open_queue:
                open_queue.append(y)
                prev[y] = x
        
        print_maze_with_path(maze, closed_set, [], start, end)
        time.sleep(0.3)
        clear_output(wait=True)
        os.system("cls")
        
        closed_set.add(x)

    print("No path found.")
    return None


# 4. Greedy Search

# In[5]:


def greedy_search(maze, start, end):
    open_queue = PriorityQueue()
    closed_set = set()
    prev = {}

    open_queue.put((h(start, end), start))
    
    while open_queue:  # Cleaner condition
        _, x = open_queue.get()  

        if x == end:
            path = reconstruct_path(prev, x)
            print_maze_with_path(maze, closed_set, path, start, end)
            print("S Start\nE End\n# Opened node\no Path\nX Wall\nspace Fresh node\n--------------")
            print(f"Nodes expanded: {len(closed_set)}")
            print(f"Path length: {len(path) - 1}")
            return path

        for y in get_neighbors(maze, x):
            if y not in closed_set and y not in [node[1] for node in open_queue.queue]:
                open_queue.put((h(y, end), y))  
                prev[y] = x

        closed_set.add(x)

        print_maze_with_path(maze, closed_set, [], start, end)
        time.sleep(0.3)
        clear_output(wait=True)
        os.system("cls")

    print("No path found.")
    return None


# 5. A*

# In[6]:


def a_star(maze, start, end):
    open_queue = PriorityQueue()
    latest_f = {} # Made due to duplicates in open_queue
    dist = {start: 0}
    prev = {}
    closed_set = set()

    open_queue.put((h(start, end), start))
    latest_f[start] = h(start, end)

    while open_queue:
        f_x, x = open_queue.get()

        if x in closed_set:
            continue

        if latest_f[x] != f_x: # We chose a duplicate
            continue  

        if x == end:
            path = reconstruct_path(prev, x)
            print_maze_with_path(maze, closed_set, path, start, end)
            print("S Start\nE End\n# Opened node\no Path\nX Wall\nspace Fresh node\n--------------")
            print(f"Nodes expanded: {len(closed_set)}")
            print(f"Path length: {len(path) - 1}")
            return path

        for y in get_neighbors(maze, x):
            if y in closed_set:
                continue

            d_new = dist[x] + 1

            if y not in latest_f or dist[y] > d_new:  
                dist[y] = d_new
                prev[y] = x
                latest_f[y] = d_new + h(y, end)
                open_queue.put((latest_f[y], y))  

        closed_set.add(x)
        
        print_maze_with_path(maze, closed_set, [], start, end)
        time.sleep(0.3)
        clear_output(wait=True)
        os.system("cls")

    print("No path found.")
    return None


# User Interface:

# In[14]:


file_name = input("Enter the maze file name: ").strip()

print("\nChoose an algorithm:")
print("1. Random Search")
print("2. DFS")
print("3. BFS")
print("4. Greedy Search")
print("5. A*")

choice = input("\nEnter the number of the algorithm (1-5): ").strip()

maze, start, end = load_maze(file_name)

if choice == "1":
    print("\nRunning Random Search...\n")
    time.sleep(1)
    path = random_search(maze, start, end)
elif choice == "2":
    print("\nRunning Depth Search (DFS)...\n")
    time.sleep(1)
    path = dfs(maze, start, end)
elif choice == "3":
    print("\nRunning Width Search (BFS)...\n")
    time.sleep(1)
    path = bfs(maze, start, end)
elif choice == "4":
    print("\nRunning Greedy Search...\n")
    time.sleep(1)
    path = greedy_search(maze, start, end)
elif choice == "5":
    print("\nRunning A* Search...\n")
    time.sleep(1)
    path = a_star(maze, start, end)
else:
    print("Invalid choice. Please enter a number between 1 and 5.")

