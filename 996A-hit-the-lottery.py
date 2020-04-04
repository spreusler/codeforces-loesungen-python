# Name: 996 A. Hit the Lottery
# URL: https://codeforces.com/problemset/problem/996/A
# Language: Python 3.x

def main():
    # Deklaration der Summe der erforderlichen Scheine
    sum_bills = 0

    # Einlesen des Input als Integer
    n = int(input())

    # Erzeugen einer Liste an moeglichen Scheinen
    bills = [100, 20, 10, 5, 1]

    # Schleife über alle moegliche Scheine
    for i in range(len(bills)):

        # Berechnung der Anzahl der Scheine
        sum_bills +=  n // bills[i]

        # Subtraktion der Werte der Scheine fuer neuen Wert n
        n -= bills[i] * (n // bills[i])

    print(sum_bills)


if __name__ == '__main__':
    main()
