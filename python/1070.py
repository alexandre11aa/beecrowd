### Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o
### X ser for o caso. A entrada será um valor inteiro positivo. A saída será uma sequência de seis números ímpares. Q:1070

dd = int(input())

for i in range(12):
	if dd % 2 != 0:
		print(dd)
	dd += 1
