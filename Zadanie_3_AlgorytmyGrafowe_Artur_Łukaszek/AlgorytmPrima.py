from heapq import heappop, heappush, heapify

def prima(neighbour_matrix):
    pred = [-1 for _ in range(len(neighbour_matrix))]
    k = [float('inf')] * len(neighbour_matrix)
    s = 0
    k[s] = 0
    pq = []
    for v in range(len(neighbour_matrix)):
        heappush(pq, (float(k[v]), v))
    pq_nodes = [x[1] for x in pq]

    while len(pq) > 0:
        u = heappop(pq)[1]
        pq_nodes.remove(u)
        for v, weight in enumerate(neighbour_matrix[u]):
            if weight != 0.0 and weight != float('inf'):
                if v in pq_nodes:
                    if weight < k[v]:
                        pred[v] = u
                        k[v] = weight
                        pq[pq_nodes.index(v)] = (weight, v)
                        heapify(pq)
    return pred, k


matrix = [[float(x) for x in line.split()] for line in open("Prima_Djikstra_input.txt").readlines()]
print(prima(matrix))