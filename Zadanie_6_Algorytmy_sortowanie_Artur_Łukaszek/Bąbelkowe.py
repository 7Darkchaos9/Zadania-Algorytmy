def Babelkowe(tab):
    for i in range(1, len(tab)):
        if(i%1000 == 0):
            print(f"{i} z {len(tab)}")
        for j in range(len(tab)-1, i-1, -1):
            if tab[j] < tab[j-1]:
                tab[j-1], tab[j] = tab[j], tab[j-1]


if __name__ == "__main__":
    tab = [9,7,2,4,13,19,15,8]
    print("Przed:")
    print(tab)
    Babelkowe(tab)
    print("Po:")
    print(tab)