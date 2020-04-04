# Name: 705 A. Hulk
# URL: https://codeforces.com/problemset/problem/705/A

def main():
    # Einlesen des Inputs als Integer Wert
    n = int(input())

    # Erzeugt eine Liste a mit n Wiederholungen
    a = ["hate", "love"] * n

    # a[:n] entspricht der Liste a bis einschließlich n-ter Stelle
    # .join() konkateniert Strings und fügt a[:n] vorne iterativ zu
    # Falls n = 1, dann wird NUR der Listenwert von a[:1] konkateniert.
    print("I"," that I ".join(a[:n]),"it")

if __name__ == '__main__':
	main()
