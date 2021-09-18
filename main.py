from GraphDijkstra import GraphD
from GraphBellmanFord import GraphB
from ventana import ventana

def main():
    """g = GraphD(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)

    D = g.dijkstra(0)

    for vertex in range(len(D)):
        print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

    g = GraphB(5)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(3, 2, 2)

    g.bellman_ford(0)"""

    ventana();

if __name__ == "__main__":
    main()
