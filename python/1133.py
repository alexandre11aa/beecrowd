### Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for ig
### ual a 2 ou igual a 3. O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescen
### te. Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente. Q:1133

n1 = int(input())
n2 = int(input())

if n2 < n1:
	xx = n2
	n2 = n1
	n1 = xx

con = n1 + 1

while con < n2:
	if con % 5 == 2 or con % 5 == 3:
		print(con)
	con += 1
