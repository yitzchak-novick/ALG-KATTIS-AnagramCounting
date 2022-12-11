import sys
from math import factorial

for line in sys.stdin:
	dict = {}
	l = line.strip()
	for c in l:
		dict[c] = dict.get(c, 0) + 1
	result = factorial(len(l))
	for k, v in dict.items():
		#print (k , v)
		result = result // factorial(v)
print(int(result))
