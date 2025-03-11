name = "Konstantynopolitańczykowianeczka"
t1 = name[11:22]
t2 = name[0:9]
print(t1)
print(t2)


# Zadania metody na stringach - Powodzenia Aleksandra!


# Zmiana wielkości liter
# Zadeklaruj zmienną tekst = "Witaj w Pythonie!" i zamień wszystkie litery na wielkie.
# 💡 Podpowiedź: Poszukaj metody, która zamienia wszystkie litery na duże.

tekst = "Witaj w Pythonie!"

t1 = tekst.upper()

print(t1)

# Sprawdzanie początku napisu
# Utwórz zmienną zdanie = "Programowanie jest fajne!" i sprawdź, czy zaczyna się od "Programowanie".
# 💡 Podpowiedź: Jest metoda, która pozwala sprawdzić początek stringa.

tekst = "Programowanie jest fajne!"

t1 = tekst.startswith("Programowanie")

print(t1)

# Sprawdzanie końca napisu
# Zadeklaruj zmienną plik = "raport.pdf" i sprawdź, czy kończy się na ".pdf".
# 💡 Podpowiedź: Podobnie jak metoda na sprawdzenie początku, istnieje metoda na sprawdzenie końca.

tekst = "raport.pdf"

t1 = tekst.endswith(".pdf")

print(t1)

# Usuwanie zbędnych spacji
# Utwórz zmienną komunikat = " To jest ważne! " i usuń zbędne spacje z początku i końca.
# 💡 Podpowiedź: Poszukaj metody, która „przycina” spacje.

tekst = " To jest ważne! "

t1 = tekst[1:15]

print(t1)

# Zliczanie wystąpień znaku
# Zadeklaruj zmienną tekst = "abrakadabra" i policz, ile razy występuje litera "a".
# 💡 Podpowiedź: Jest metoda licząca wystąpienia danego znaku w stringu.

tekst = "abrakadabra"

t1 = tekst.count("a")
print(t1)

# Podmiana fragmentu tekstu
# Utwórz zmienną zdanie = "Lubię jabłka" i zamień "jabłka" na "gruszki".
# 💡 Podpowiedź: Poszukaj metody, która pozwala zamieniać fragmenty stringa.

zdanie = "Lubię jabłka" 

t1 = zdanie.replace("Lubię jabłka", "Lubię gruszki")

print(t1)

# Łączenie wyrazów
# Mając listę wyrazy = ["Python", "jest", "super"], połącz je w jedno zdanie, oddzielając spacjami.
# 💡 Podpowiedź: Istnieje metoda, która pozwala połączyć elementy listy w string.

wyrazy = ["Python", "jest", "super"]

t1 = " ".join(wyrazy)

print(t1)

# Znajdowanie indeksu słowa
# Zadeklaruj zmienną tekst = "Uczę się programowania w Pythonie" i znajdź pozycję, na której występuje słowo "Python".
# 💡 Podpowiedź: Poszukaj metody, która zwraca indeks pierwszego wystąpienia podanego fragmentu.

tekst = "Uczę się programowania w Pythonie"

t1 = tekst.find("Python")

print(t1)
