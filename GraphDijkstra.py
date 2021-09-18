from queue import PriorityQueue

class GraphD:

    def add_edge(self, u, v, weight):
         self.edges[u][v] = weight
         self.edges[v][u] = weight

    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    def print_bellman(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.v):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.v
        dist[src] = 0

        for _ in range(self.v - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.edges:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)
