# Function to calculate total distance of a given route
def calculate_total_distance(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + distance_matrix[route[-1]][route[0]]

# Function to generate all permutations of a list
def generate_permutations(arr, start, end, result):
    if start == end: result.append(arr[:])
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start + 1, end, result)
            arr[start], arr[i] = arr[i], arr[start]

# Main function to solve TSP
def traveling_salesman_problem():
    n = int(input("Enter the number of cities: "))
    distance_matrix = [[int(input(f"Distance from city {i+1} to city {j+1}: ")) if i != j else 0 for j in range(n)] for i in range(n)]
    
    cities = list(range(n))
    all_routes = []
    generate_permutations(cities, 0, n - 1, all_routes)
    
    best_route = min(all_routes, key=lambda route: calculate_total_distance(route, distance_matrix))
    min_distance = calculate_total_distance(best_route, distance_matrix)
    
    print(f"The best route is: {'-> '.join(str(city + 1) for city in best_route)}")
    print(f"The minimum total distance is: {min_distance}")

# Call the TSP function to execute the program
traveling_salesman_problem()
