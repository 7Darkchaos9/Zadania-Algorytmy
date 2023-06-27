from random import randint
def Scalanie(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Scalanie(L)
        Scalanie(P)
        Scal(tab, L, P)


def Scal(tab, L, P):
    i = j = k = 0
    while i < len(L) and j < len(P):
        if L[i] < P[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = P[j]
            j += 1
        k += 1

    while i < len(L):
        tab[k] = L[i]
        i += 1
        k += 1

    while j < len(P):
        tab[k] = P[j]
        j += 1
        k += 1


if __name__ == "__main__":
    tab = [9,7,2,4,13,19,15,8]
    print("Przed:")
    print(tab)
    Scalanie(tab)
    print("Po:")
    print(tab)