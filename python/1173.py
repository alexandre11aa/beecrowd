### Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente,c
### oloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim
### sucessivamente. Mostre o vetor em seguida. A entrada contém um valor inteiro (V<=50). Para cada posição do vetor, escreva "N[i
### ] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o v
### alor de V. Q:1173

v = []

nmr = int(input())

for i in range(10):
	v.append(nmr)
	print("N[%.f] = %.f" % (i,v[i]))
	nmr *= 2
