# Podaj nazwę pliku wejściowych danych.
# Plik danych wejściowych musi znajdować się w tym samym folderze.
plik_nazwa = input()
with open(f'{plik_nazwa}', 'r') as plik:
    wiersze = plik.readlines()

# Liczba sloni n.
n_slonie = int(wiersze[0][:-1])

# Masa każdego słonia m(i).
m_slonie = wiersze[1][:-1].split(sep=' ')
m_slonie = [int(i) for i in m_slonie]

# Ustawienie pracowników a(1).
kolej_a = wiersze[2][:-1].split(sep=' ')
kolej_a = [int(i) for i in kolej_a]

# Ustawienie Dyrektora b(1).
kolej_b = wiersze[3][:-1].split(sep=' ')
kolej_b = [int(i) for i in kolej_b]

# Każdą permutację można podzielić na proste cykle.
cykle = []
lista_index = []

# Permutacja przez indeksy.
for numer in range(1, n_slonie + 1):
    if numer in lista_index:
        continue
    i_lista = kolej_b.index(numer)
    waga_slonia = [m_slonie[numer-1]]

    while True:
        if kolej_a[i_lista] == numer:
            break

        poprawny_index = kolej_a[i_lista]

        if poprawny_index not in lista_index:
            lista_index.append(poprawny_index)
        waga_slonia.append(m_slonie[poprawny_index-1])
        i_lista = kolej_b.index(poprawny_index)

    cykle.append(waga_slonia)


# Zastosowanie pierwszej metody.
def metoda_1(cykl):
    return sum(cykl)+(len(cykl)-2)*min(cykl)


# Zastosowanie drugiej metody.
def metoda_2(cykl):
    return sum(cykl)+min(cykl)+int((len(cykl)+1)*min(m_slonie))


wynik = 0
for cykl in cykle:
    wynik += min(metoda_1(cykl), metoda_2(cykl))

print(wynik)
# Wynik można porównać z plikiem w folderze "Pliki danych wyjściowych".