import random

# Funkcja obliczająca odległość między dwoma miastami (przykładowa implementacja)
def distance(city1, city2):
    # Tutaj można zaimplementować własną funkcję obliczającą odległość między miastami
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

# Funkcja oceny (fitness) - suma odległości trasy
def evaluate_route(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(cities[route[i]], cities[route[i + 1]])
    total_distance += distance(cities[route[-1]], cities[route[0]])
    return total_distance

# Funkcja generująca początkową populację losowych tras
def generate_initial_population(num_routes, num_cities):
    population = []
    for _ in range(num_routes):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population

# Funkcja krzyżowania (przykładowa implementacja PMX)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)

    for i in range(start, end + 1):
        child[i] = parent1[i]

    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(parent2)):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break

    return child

# Funkcja mutacji (przykładowa implementacja - zamiana dwóch losowych miast)
def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]
    return route

# Algorytm genetyczny
def genetic_algorithm(cities, num_generations, population_size):
    num_cities = len(cities)
    population = generate_initial_population(population_size, num_cities)

    for generation in range(num_generations):
        population = sorted(population, key=lambda x: evaluate_route(x, cities))
        new_population = population[:population_size // 2]

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Prawdopodobieństwo mutacji
                child = mutate(child)
            new_population.append(child)

        population = new_population

    best_route = min(population, key=lambda x: evaluate_route(x, cities))
    best_distance = evaluate_route(best_route, cities)
    return best_route, best_distance

if __name__ == "__main__":
    # Przykładowa lista miast w formacie (x, y)
    cities = [(0, 0), (1, 2), (2, 4), (3, 1), (5, 3)]

    best_route, best_distance = genetic_algorithm(cities, num_generations=1000, population_size=100)
    print("Najlepsza trasa:", best_route)
    print("Najlepsza odległość:", best_distance)