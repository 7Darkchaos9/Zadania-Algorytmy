tab = [1.4, 2.4, 6.1, 4.8, 3.4, 7.9, 5.2, 4.4]
najw = tab[0]

for i in tab:
    if najw < i:
        najw = i

print("Największa liczbą jest: " + str(najw))