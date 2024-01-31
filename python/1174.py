### Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a
### 10 e o valor armazenado em cada uma das posições. A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou nega
### tivos. Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenadon
### a posição, com uma casa após o ponto decimal. Q:1174

v = []

for i in range(101):
	nmr = float(input())
	v.append(nmr)

for j in range(101):
	if v[j] <= 10:
		print("A[%.i] = %.1f" % (j,v[j]))
