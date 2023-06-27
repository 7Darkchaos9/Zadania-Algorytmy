kod = {"A": "", "B": "", "C": "", "D": "", "E": "", }
symbole = [(30, "A"), (10, "B"), (10, "C"), (20, "D"), (30, "E")]

def ShannonFano(symbole):
    if len(symbole) > 1:
        symbole = sorted(symbole, reverse=True)
        lewo = []
        sumal = 0
        prawo = symbole
        sumap = 0
        for znak in prawo:
            sumap += znak[0]
        i = 0
        while i < len(symbole):
            if abs((sumal + prawo[0][0]) - (sumap - prawo[0][0])) < abs(sumal - sumap):
                s = prawo.pop(0)
                lewo.append(s)
                sumal += s[0]
                sumap -= s[0]
                i += 1
            else:
                break
        for znak in lewo:
            kod[znak[1]] += "0"
        for znak in prawo:
            kod[znak[1]] += "1"
        ShannonFano(lewo)
        ShannonFano(prawo)


ShannonFano(symbole)
print("Kod: ", kod)
tekst = "ABCD"
print("Tekst: ", tekst, "\nZakodowany tekst: ", end="")
for litera in tekst:
    print(kod[litera], end="")