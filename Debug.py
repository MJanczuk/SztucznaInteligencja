import itertools

def DrogaWglab(BADANA_LISTA_ODLEGLOSCI, KOLEJNOSC):
    Suma = 0.0
    for i in range(len(KOLEJNOSC) - 1):
        Suma = Suma + BADANA_LISTA_ODLEGLOSCI[KOLEJNOSC[i]][KOLEJNOSC[i + 1]]
    return (Suma)

LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI = [[0.0, 136.0, 143.6, 91.2], [136.0, 0.0, 145.3, 87.8], [143.6, 145.3, 0.0, 69.4], [91.2, 87.8, 69.4, 0.0]]

AKTUALNA_KOLEJNOSC = []
for a in range(len(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI)):
    AKTUALNA_KOLEJNOSC.append(a)

AKTUALNA_DROGA = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, AKTUALNA_KOLEJNOSC)
print('Algorytm wgłąb       : ', AKTUALNA_KOLEJNOSC, AKTUALNA_DROGA)

A = itertools.permutations(AKTUALNA_KOLEJNOSC)
for a in A:
    TestowanaDroga = DrogaWglab(LISTA_ODLEGLOSCI_MIEDZY_MIASTAMI, a)
    if TestowanaDroga<AKTUALNA_DROGA:
        AKTUALNA_KOLEJNOSC = a
        AKTUALNA_DROGA = TestowanaDroga
        print('Algorytm wgłąb       : ', AKTUALNA_KOLEJNOSC, AKTUALNA_DROGA)
