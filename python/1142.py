### Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução d
### o programa. O arquivo de entrada contém um número inteiro positivo N. Imprima a saída conforme o exemplo fornecido. Q:1142

a = 1
b = 2
c = 3

nmr = int(input())

for x in range(0,nmr):
	print("%.f %.f %.f PUM" % (a,b,c))
	a += 4
	b += 4
	c += 4
