def boyermoore(tekst, wzorzec):
    m = len(wzorzec)
    i = m-1
    j = m-1
    while i < len(tekst):
        while tekst[i] == wzorzec[j]:
            i-=1
            j-=1
        if j == -1:
            return i+1
        else:
            i += m - min(j, 1+prz(tekst[i]))
            j = m-1
    return -1

def prz(litera):
    for l in p.keys():
        if l == litera:
            return p[litera]
    return -1

tekst = "wyszukiwanie wzorca"
wzorzec = "wzor"

p = {litera:index for index, litera in enumerate(wzorzec)}
print(boyermoore(tekst, wzorzec))

