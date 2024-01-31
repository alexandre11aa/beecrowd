#### Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, isóceleso
#### u equilátero e se trata-se de um triângulo retângulo ou não. A entrada consiste em três números inteiros A,B e C (0 < A,B,C <1
#### 05). A saída deve conter a string "Invalido" se os valores lidos não formarem um triângulo. Se os valores formarem um triângul
#### o a saída deve ser "Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica do triângulo seg
#### uido de "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" se não for, conforme os exemplos. Q:2313

a, b, c = map(int,input().split())

if c > b:
	x = b
	b = c
	c = x

if b > a:
	x = a
	a = b
	b = x

if c > b:
	x = b
	b = c
	c = x

if (a < b + c) and (b < a + c) and (c < a + b):
	if a != b != c:
		if a**2 == b**2 + c**2:
			print("Valido-Escaleno")
			print("Retangulo: S")
		else:
			print("Valido-Escaleno")
			print("Retangulo: N")
	elif a == b == c:
		print("Valido-Equilatero")
		print("Retangulo: N")
	else:
		if a**2 == b**2 + c**2:
			print("Valido-Isoceles")
			print("Retangulo: S")
		else:
			print("Valido-Isoceles")
			print("Retangulo: N")
else:
	print("Invalido")
