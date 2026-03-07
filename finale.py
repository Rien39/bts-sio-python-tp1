def trier_sommes(liste):
    return sorted(liste)
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))
d = int(input("Entrez d : "))
e = int(input("Entrez e : "))
sommes = [a, b, c, d, e]
sommesT = trier_sommes(sommes)
print(sommesT)