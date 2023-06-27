from heapq import heappush, heappop
def Stogowe(tab):
    heap = []
    for value in tab:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]


if __name__ == "__main__":
    tab = [9,7,2,4,13,19,15,8]
    print("Przed:")
    print(tab)
    tab = Stogowe(tab)
    print("Po:")
    print(tab)