#Stwórz zmienna o typie danych string, o wartości "Świat_jest_mały. 
# Zdecydowanie za mały, żeby nie uczyć się Pythona" i wyłuskaj wartość "Pythona", "Świat" 
# oraz "typie danych string" następnie wyprintuj do konsoli obie te nazwy w ramach osobnych zmiennych

text = "Świat_jest_mały. Zdecydowanie za mały, żeby nie uczyć się Pythona"

z1 = text[0:5]
z2 = text[58:65]

#print(z1)
#print(z2)


# Zadania - metody na stringach - Powodzenia Kacper!

# Zmiana wielkości pierwszej litery
# Utwórz zmienną tekst = "python to fajny język" i zmień tylko pierwszą literę na wielką.
# 💡 Podpowiedź: Poszukaj metody, która zmienia wielkość pierwszej litery.

tekst = "python to fajny język"
print(tekst.capitalize())

# Zamiana wszystkich znaków na małe
# Zadeklaruj zmienną wiadomosc = "PYTHON JEST ŚWIETNY!" i zamień wszystkie litery na małe.
# 💡 Podpowiedź: Poszukaj metody, która zamienia wszystkie litery na małe.

wiadomosc = "PYTHON JEST ŚWIETNY!"
print(wiadomosc.lower())

# Usuwanie znaków specjalnych
# Utwórz zmienną dane = "---Python---" i usuń z niej znak "-" z początku i końca.
# 💡 Podpowiedź: Jest metoda, która usuwa określone znaki z krańców stringa.

dane = "---Python---"
print(dane.strip("-"))

# Zliczanie długości tekstu
# Zadeklaruj zmienną napis = "Ile to ma znaków?" i policz, ile ma znaków (łącznie ze spacjami).
# 💡 Podpowiedź: W tym przypadku nie potrzebujesz metody na stringu, ale wbudowaną funkcję Pythona.

napis ="Ile to ma znaków?"
print(len(napis))

# Podmiana znaku w napisie
# Utwórz zmienną tekst = "banana" i zamień wszystkie litery "a" na "o".
# 💡 Podpowiedź: Użyj metody, która pozwala zamienić jeden znak na inny.

tekst = "banana"
print(tekst.replace("a","o"))

# Podział tekstu na części
# Mając zmienną zdanie = "To jest przykładowe zdanie", podziel je na osobne wyrazy.
# 💡 Podpowiedź: Poszukaj metody, która zwraca listę wyrazów.

zdanie = "To jest przykładowe zdanie"
print(zdanie.rsplit())

# Sprawdzanie, czy tekst zawiera tylko cyfry
# Zadeklaruj zmienną numer = "12345" i sprawdź, czy zawiera tylko cyfry.
# 💡 Podpowiedź: Istnieje metoda, która sprawdza, czy string składa się wyłącznie z cyfr.

numer = "12345"
print(numer.isdigit())

# Usuwanie znaków nowej linii
# Mając zmienną wiersz = "To jest wiersz.\n", usuń z niego znak nowej linii (\n).
# 💡 Podpowiedź: Poszukaj metody, która usuwa określone znaki z końca stringa.

wiersz = "To jest wiersz.\n"
print(wiersz.rstrip("\n"))