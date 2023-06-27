symbole = [(30, "A"), (10, "B"), (20, "C"), (10, "D"), (20, "E"), (10, "F")]
kod = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": ""}
symbole = sorted(symbole, reverse=True)
while len(symbole) > 1:
    symbol1 = symbole.pop()
    symbol2 = symbole.pop()
    for znak in symbol1[1]:
        kod[znak] = "0" + kod[znak]
    for znak in symbol2[1]:
        kod[znak] = "1" + kod[znak]
    s1s2 = (symbol1[0] + symbol2[0], symbol1[1] + symbol2[1])
    symbole.append(s1s2)
    symbole = sorted(symbole, reverse=True)

print(kod)
tekst = "ABCD"
print("Tekst: ", tekst)
print("Zakodowany tekst: ", end="")
for znak in tekst:
    print(kod[znak], end="")