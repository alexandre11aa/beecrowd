### Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloq
### ue a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N. A entrada contem um valor d
### e dupla precisão com 4 casas decimais. Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o v
### alor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais. Q:1178

v = []

nmr = float(input())

for i in range(100):
	v.append(nmr)
	nmr /= 2

for j in range(100):
	print("N[%.f] = %.4f" % (j,v[j]))
