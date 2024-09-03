### Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T - 1 repetidas vezes, co
### nforme exemplo abaixo. Imprima o vetor N. A entrada contém um valor inteiro T (2 ≤ T ≤ 50). Para cada posição do vetor, escrev
### a "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição. Q:1177

v = []
con = 1

nmr = int(input())

while con <= 1000:
	con1 = 0

	for j in range(nmr):
		v.append(con1)
		con1 +=1

	con += nmr

for i in range(1000):
	print("N[%.f] = %.f" % (i,v[i]))
