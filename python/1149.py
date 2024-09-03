### Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A para cada i com os valores (0 <= i <= N-1). EnquantoN
### for negativo ou ZERO, um novo N(apenas N) deve ser lido. A entrada contém somente valores inteiros, podendo ser positivos ou n
### egativos. Todos os valores estão na mesma linha. A saída contém apenas um valor inteiro. Q:1149

con = True

t = input()

t1 = t.split()

n = int(t1[0])
a1 = 1

while con == True:
	if int(t1[a1]) > 0:
		a = int(t1[a1])
		con = False
	else:
		a1 += 1

con1 = 1
soma = n
total = 0

while con1 <= a:
	total += soma
	soma += 1
	con1 += 1

print(total)
