### Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo al
### ógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados. O arquivo de entrada con
### tém um número inteiro positivo N (1 < N < 1000). Imprima a saída conforme o exemplo fornecido. Q:1144

a = 1

nmr = int(input())

for x in range(0,nmr):
	b = a**2
	c = a**3
	bb = b + 1
	cc = c + 1
	print(a,b,c)
	print(a,bb,cc)
	a += 1
