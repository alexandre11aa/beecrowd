### Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, inc
### luindo ambos. O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente. Imprima a soma
### de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso. Q:1132

x = float(input())
y = float(input())

if y > x:
	xx = x
	x = y
	y = xx

con = y
soma = 0

while con <= x:
	if con % 13 != 0:
		soma += con
	con += 1

print(int(soma))
