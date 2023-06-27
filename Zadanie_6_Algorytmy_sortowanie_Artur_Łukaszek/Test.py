import time
import random
from Wstawianie import Wstawianie
from Bąbelkowe import Babelkowe
from Szybkie import Szybkie
from Stogowe import Stogowe
from Scalanie import Scalanie


def gen_array(size):
    tab = []
    for i in range(1, size):
        tab.append(random.randint(1, size))
    return tab


def test():
    print("** Dla wielkości 1 000 **")
    for i in range(0, 5):
        if i == 0:
            print("Wystawianie: ")
        elif i == 1:
            print("\nBąbelkowe: ")
        elif i == 2:
            print("\nSzybkie: ")
        elif i == 3:
            print("\nStogowe: ")
        else:
            print("\nScalanie: ")
        tab = []
        czas = []
        for j in range(0, 3):
            tab = gen_array(1_000)
            start = time.perf_counter()
            if i == 0:
                Wstawianie(tab)
            elif i == 1:
                Babelkowe(tab)
            elif i == 2:
                Szybkie(tab, 0, len(tab) - 1)
            elif i == 3:
                Stogowe(tab)
            else:
                Scalanie(tab)
            stop = time.perf_counter()
            czas += [stop - start]
        print("Czasy [s]:", [round(j, 10) for j in czas])
        print("Średnia [s]:", round(sum(czas) / len(czas), 10))

    print("\n\n** Dla wielkości 100 000 **")
    for i in range(0, 5):
        if i == 0:
            print("Wstawianie: ")
        elif i == 1:
            print("\nBąbelkowe: ")
        elif i == 2:
            print("\nSzybkie: ")
        elif i == 3:
            print("\nStogowe: ")
        else:
            print("\nScalanie: ")
        tab = []
        czas = []
        for j in range(0, 3):
            tab = gen_array(100_000)
            start = time.perf_counter()
            if i == 0:
                Wstawianie(tab)
            elif i == 1:
                Babelkowe(tab)
            elif i == 2:
                Szybkie(tab, 0, len(tab) - 1)
            elif i == 3:
                Stogowe(tab)
            else:
                Scalanie(tab)
            stop = time.perf_counter()
            czas += [stop - start]
        print("Czasy [s]:", [round(j, 10) for j in czas])
        print("Średnia [s]:", round(sum(czas) / len(czas), 10))


test()