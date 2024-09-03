### Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para ca
### da par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M). O arqu
### ivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negat
### ivo. Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles. Q:1101
	
con = True

while con == True:
	soma = 0
	n, m = map(int,input().split())
	if n <= 0 or m <= 0:
		con = False
	else:
		if n < m:
		x = n
		n = m
		m = x
	nmr = m
	while nmr <= n:
		print(nmr, end=' ')
		soma += nmr
		nmr += 1
	print("Sum=%.f" % soma)
