# Name: 791 A. Bear and Big Brother
# URL: https://codeforces.com/problemset/problem/791/A
# Language: Python 3.x

def main():
    # Einlesen der Zahlen und Split bei Leerzeichen
    # Umwandlung von input().split(" ") in Integer Zahlen via map() Funktion
    a, b = map(int, input().split(" "))

    # Zuweisung Startjahr = 0
    year = 0

    # Schleife: Solange b groesser oder gleich a ist
    while a <= b:
        # Multiplikation mit sich selbst und der Zahl 3 bzw. 2
        a *= 3
        b *= 2
        # Jahr Addition mit sich selbst und Zahl 1 als Counter
        year += 1

    # Ausgabe des Jahres
    print(year)

if __name__ == '__main__':
	main()                                                                                                                                                                                                                                                        
