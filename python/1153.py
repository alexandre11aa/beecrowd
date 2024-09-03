### Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1. A entrada co
### ntém um valor inteiro N (0 < N < 13). A saída contém um valor inteiro, correspondente ao fatorial de N. Q:1153

n = int(input())
x = n - 1

for i in range(n):
	if x != 0:
		n *= x
		x -= 1

print(n)
