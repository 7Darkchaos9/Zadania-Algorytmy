def cezar(tekst, alfabet, przesuniecie):
    for znak in tekst:
        if znak in alfabet:
            print(alfabet[(alfabet.find(znak)+przesuniecie)%(len(alfabet))], end='')
        else:
            print(znak, end='')

tekst = "Tekst do zakodowania"
alfabet = "abcdefghijklmnopqrstuvwxyz"
przesuniecie = 6
cezar(tekst, alfabet, przesuniecie)