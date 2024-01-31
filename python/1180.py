### Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontr
### e o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação. A primeira linha de entrada contemu
### m único inteiro N (1 < N < 1000), indicando o número de elementos que deverão ser lidos em seguida para o vetor X[N] de inteir
### os. A segunda linha contém cada um dos N valores, separados por um espaço. A primeira linha apresenta a mensagem “Menor valor:
### ” seguida de um espaço e do menor valor lido na entrada. A segunda linha apresenta a mensagem “Posicao:” seguido de um espaçoe
### da posição do vetor na qual se encontra o menor valor lido, lembrando que o vetor inicia na posição zero. Q:1180
		
nmr = int(input())
nmrs = input()

lista = nmrs.split()

x = 9 * (10**999999)
y = 0

for i in range(nmr):
	z = int(lista[i])
	if  x > z:
		x = z
		y = i

print("Menor valor: %.f" % x)
print("Posicao: %.f" % y)
