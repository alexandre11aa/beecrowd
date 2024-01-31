### Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentada
### s na execução do programa. O arquivo de entrada contém um número inteiro positivo N. Imprima a saída conforme o exemplo fornec
### ido. Q:1143

a = 1

nmr = int(input())

for x in range(0,nmr):
	b = a**2
	c = a**3
	print(a,b,c)
	a += 1
