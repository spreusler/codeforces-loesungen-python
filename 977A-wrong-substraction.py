# Name: 977 A. Wrong Subtraction
# URL: https://codeforces.com/problemset/problem/977/A
# Language: Python 3.x

def main():
	# Einlesen der zwei Zahlen n und k
	# Umwandlung von input().split(" ") in Integer Zahlen via map()-Funktion
	n,k = map(int,input().split(" "))

	#Iteriere über n in k Anzahl
	for i in range(k):
		# Wenn der Divisionsrest von n dividiert durch 10 gleich Null ist
		# Modulo Operator
		if n % 10 == 0:
			# Division von n durch 10
			n //= 10
		# Subtraktion von n
		else:
			n -= 1
	print(n)


if __name__ == '__main__':
	main()
