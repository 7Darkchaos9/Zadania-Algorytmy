def karparabina(tekst, wzorzec, q):
    prime = 19
    tekst_hash = 0
    wzorzec_hash = 0
    m = len(wzorzec)

    for i in range(m):
        wzorzec_hash = (wzorzec_hash * len(q) + q[wzorzec[i]]) % prime
        tekst_hash = (tekst_hash * len(q) + q[tekst[i]]) % prime

    i = 0
    while i <= len(tekst) - len(wzorzec):
        if tekst_hash == wzorzec_hash:
            if tekst[i:i + len(wzorzec)] == wzorzec:
                return i
        tekst_hash = ((tekst_hash - (q[tekst[i]] * pow(len(q), m - 1))) * len(q) + q[
            tekst[i + m]]) % prime

        i += 1
    return -1


tekst = "wyszukiwanie wzorca"
wzorzec = "wzor"
q = {}
for y, x in enumerate(tekst):
    if x not in q.keys(): q[x] = y;
print(karparabina(tekst, wzorzec, q))