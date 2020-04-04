# Name: 1030 A. In Search of an Easy Problem
# URL: https://codeforces.com/problemset/problem/1030/A
# Language: Python 3.x

def main():
    # Erste Zeile einlesen
    input()

    # Zweite Zeile einlesen
    # Info: input() gibt Liste zurück
    #
    # ['1' in input()] Überprüft, ob '1' ein Element in der Liste der input-Funktion ist
    # Diese Abfrage Gibt True oder False zurück
    # https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
    #
    # True oder False kann auch als 0 und 1 codiert sein
    # Mithilfe des Index bei dem Tupel ('EASY','HARD')
    # können wir nun EASY -> False (0) oder Hard -> True (1) anfragen
    # https://python-reference.readthedocs.io/en/latest/docs/brackets/indexing.html
    print(('EASY', 'HARD')['1' in input()])

if __name__ == '__main__':
	main()
