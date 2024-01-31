### Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o
### caso. O arquivo de entrada contém 1 valor inteiro qualquer. Imprima todos os valores ímpares de 1 até X, inclusive X, se for o
### caso. Q:1067

cc = float(input())
con = 1
impares = 1

if cc <= 0:
	print("Informe um número positivo não nulo.")
else:
	while con <= cc:
		print(impares)
		con += 2
		impares += 2
