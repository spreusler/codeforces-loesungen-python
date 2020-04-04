# Name: 785 A. Anton and Polyhedrons
# URL: https://codeforces.com/problemset/problem/785/A

def main():
    # Variable fuer Summe der Flächen
    sum_faces = 0

    # Einlesen des Inputs als Integer
    n = int(input())

    # Erstellung eines Dictionaries mit Keys als String und Values as Integer
    faces = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20,
        }

    # Solange n groesser als Null ist Schleife. Ende wenn n gleich Null
    while n > 0:
        # Aufsummieren der einzelnen Values durch Key Abfrage von input()
        sum_faces += faces[input()]

        # Herunterzaehlen. Wenn n gleich Null, erfolgt kein input() Aufruf mehr
        n -= 1

    print(sum_faces)

if __name__ == '__main__':
    main()
