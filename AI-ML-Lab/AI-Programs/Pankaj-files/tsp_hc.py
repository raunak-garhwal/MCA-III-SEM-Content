import random
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(path, cities):
    distance_sum = 0
    for i in range(len(path) - 1):
        distance_sum += distance(cities[path[i]], cities[path[i + 1]])
    distance_sum += distance(cities[path[-1]], cities[path[0]])
    return distance_sum

def hill_climbing(cities):
    current_solution = list(range(len(cities)))
    random.shuffle(current_solution)
    current_distance = total_distance(current_solution, cities)

    while True:
        neighbors = []
        for i in range(len(current_solution)):
            for j in range(i + 1, len(current_solution)):
                neighbor = current_solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
                
        best_neighbor = None
        best_distance = current_distance

        for neighbor in neighbors:
            neighbor_distance = total_distance(neighbor, cities)
            if neighbor_distance < best_distance:
                best_distance = neighbor_distance
                best_neighbor = neighbor

        if best_neighbor is not None:
            current_solution = best_neighbor
            current_distance = best_distance
        else:
            break

    return current_solution, current_distance

if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))

    cities = []
    for i in range(num_cities):
        x, y = map(float, input(f"Enter the coordinates of city {i+1} (x, y): ").split(","))
        cities.append((x, y))

    best_path, best_distance = hill_climbing(cities)
    
    print(f"Best path: {best_path}")
    print(f"Best distance: {best_distance}")
