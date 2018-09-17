import sys

def add(a, b):	
	try:
		a = int(a)
		b = int(b)
		return a + b
	except ValueError:
		return "Invalid arguments"

try:
	print(add(sys.argv[1], sys.argv[2]))
except IndexError:
	print("Not enough arguments")
