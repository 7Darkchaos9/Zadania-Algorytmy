def Wstawianie(tab):
    for i in range(1, len(tab)):
        if(i%1000 == 0):
            print(f"{i} z {len(tab)}")
        j = i
        karta = tab[j]
        while(j>0 and tab[j-1] > karta):
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = karta

if __name__ == "__main__":
    tab = [9,7,2,4,13,19,15,8]
    print("Przed:")
    print(tab)
    Wstawianie(tab)
    print("Po:")
    print(tab)