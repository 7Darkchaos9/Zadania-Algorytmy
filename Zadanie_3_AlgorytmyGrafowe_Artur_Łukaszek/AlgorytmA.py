graf1 =  [[0, 5, 0, 1, 0, 0, 0, 0],
          [0, 0, 2, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 3],
          [0, 0, 0, 0, 1, 2, 0, 0],
          [0, 0, 4, 0, 0, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 2, 0, 0, 0]]


def A(graf, size, dys1):
    INF = 9_999_999_999
    pred = [0] * size
    dys = [INF] * size
    dys[0] = 0
    dys2 = [INF] * size
    dys2[0] = dys1[0]
    X = [0] * size
    X[0] = 1
    Y = [0] * size
    elements = [0] * size
    for x in range(0, size):
        elements[x] = x + 1
    print("    v", elements)

    while X != [0] * size:
        dysMin = INF
        w = 0
        for i in range(size):
            if dys2[i] < dysMin and X[i] != 0:
                dysMin = dys2[i]
                w = X[i] - 1

        for j in range(size):
            if graf[w][j] != 0 and Y[j] == 0:
                X[j] = j + 1

                d1 = dys[w] + graf[w][j]
                if d1 < dys[j]:
                    dys[j] = d1

                d2 = d1 + dys1[j]
                if d2 < dys2[j]:
                    dys2[j] = d2
                    pred[j] = w + 1

        X[w] = 0
        Y[w] = w + 1

    print(" pred", pred)
    print("dys1", dys1)
    print(" dys", dys)
    print("dys2", dys2)
    print("")


A(graf1, 8, [4, 8, 3, 4, 5, 2, 1, 0])
