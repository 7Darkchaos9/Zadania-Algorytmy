from heapq import heappop, heappush, heapify


def dijkstra(neighbour_matrix):
    pred = [-1] * len(neighbour_matrix)
    dist = [float('inf')] * len(neighbour_matrix)
    Q = [(float('inf'), i) for i in range(len(neighbour_matrix))]
    Q_nodes = [x[1] for x in Q]
    s = 0
    dist[s] = 0
    Q[Q_nodes.index(s)] = (0, s)
    heapify(Q)

    while len(Q) > 0:
        v = heappop(Q)[1]
        Q_nodes.remove(v)
        for u, weight in enumerate(neighbour_matrix[v]):
            if weight != 0.0 and weight != float('inf'):
                d = dist[v] + neighbour_matrix[v][u]
                if d < dist[u]:
                    dist[u] = d
                    pred[u] = v
    return pred, dist


matrix = [[float(x) for x in line.split()] for line in open("Prima_Djikstra_input.txt").readlines()]
print(f"pred: {dijkstra(matrix)[0]}, dist: {dijkstra(matrix)[1]}")

