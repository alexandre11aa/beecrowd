### Ler um número inteiro N e calcular todos os seus divisores. O arquivo de entrada contém um valor inteiro. Escreva todos os div
### isores positivos de N, um valor por linha. Q:1157

n = int(input())

for i in range(1,n+1):
	if n % i == 0:
		print(i)
