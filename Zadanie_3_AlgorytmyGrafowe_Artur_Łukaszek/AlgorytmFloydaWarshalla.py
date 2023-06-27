i = 9_999_999_999

d1 = [[0, 1, 5, i, i, i, i],
      [i, 0, 2, i, i, i, i],
      [i, i, 0, i, i, i, i],
      [7, i, i, 0, 1, i, i],
      [i, i, i, i, 0, 1, i],
      [2, i, i, 4, i, 0, i],
      [6, i, i, i, i, 3, 0]]

p2 = [[0, 1, 1, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [4, 0, 0, 0, 4, 0, 0],
      [0, 0, 0, 0, 0, 5, 0],
      [6, 0, 0, 6, 0, 0, 0],
      [7, 0, 0, 0, 1, 7, 0]]


def FloydWarshall(d, p, size):
    for j in range(size):
        for k in range(size):
            if j != k:
                for l in range(size):
                    if l != j and l != k:
                        path = d[k][j] + d[j][l]
                        if path < d[k][l]:
                            d[k][l] = path
                            p[k][l] = p[j][l]

    for x in range(size):
        for y in range(size):
            if d[x][y] == i:
                d[x][y] = -1

    print("\n'-1' = nieskończoność \n\nGraf d: ")
    for x in range(size):
        for y in range(size):
            print(f" {d[x][y]:^3} ", end="|")
        print("\n")

    print("Graf p: ")
    for x in range(size):
        for y in range(size):
            print(f" {p[x][y]:^3} ", end="|")
        print("\n")


FloydWarshall(d1, p2, 7)
