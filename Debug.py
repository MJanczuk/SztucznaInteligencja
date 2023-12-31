input_elements = ['A','B','C']

def Lista_Mozliwosci(NumerMiasta):
    n = len(NumerMiasta)
    c = [0] * n
    Wynik = [NumerMiasta[:]]
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                NumerMiasta[0], NumerMiasta[i] = NumerMiasta[i], NumerMiasta[0]
            else:
                NumerMiasta[c[i]], NumerMiasta[i] = NumerMiasta[i], NumerMiasta[c[i]]

            Wynik.append(NumerMiasta[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return Wynik

# Example usage:
result = Lista_Mozliwosci(input_elements)
print(result)