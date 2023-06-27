from random import randint
def Szybkie(tab, left, right):
    if left < right:
        m = left
        for i in range (left+1, right+1):
            if tab[i] < tab[left]:
                m += 1
                tab[m], tab[i] = tab[i], tab[m]
        tab[left], tab [m] = tab[m], tab[left]
        Szybkie(tab, left, m-1)
        Szybkie(tab, m+1, right)

if __name__ == "__main__":
    tab = [9,7,2,4,13,19,15,8]
    print("Przed:")
    print(tab)
    Szybkie(tab, 0, len(tab)-1)
    print("Po:")
    print(tab)