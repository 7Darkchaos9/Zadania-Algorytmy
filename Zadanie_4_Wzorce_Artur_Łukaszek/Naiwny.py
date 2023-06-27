def naiwny(text, key):
    i = 0
    j = 0
    x = len(text)
    y = len(key)
    while(j<y and i<x):
        if text[i] == key[j]:
            i+=1
            j+=1
        else:
            i -= (j-1)
            j = 0
    if j==y:
        print(f"Znaleziono wzorzec na pozycji {i-y}")
    else:
        print("Nie znaleziono wzorca")

naiwny("wyszukiwanie wzorca", "wzor")