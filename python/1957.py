#### Os dados armazenados no computador estão em binário. Uma forma econômica de ver estes números é usar a base 16 (hexadecimal).
#### Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.A
#### entrada é um número inteiro positivo V na base 10 (1 ≤ V ≤ 2 x 109). A saída é o mesmo número V na base 16 em uma única linha
#### (não esqueça do caractere de fim-de-linha). Use letras maiúsculas. Q:1957

dec = int(input())

let = ["A","B","C","D","E","F"]

if dec <= 9:
	hex = dec
	print(hex)

elif 9 < dec <= 15:
	hex = dec - 10
	print(let[hex])

else:
	hex = ""
	d3c = dec

	while d3c > 15:
		di = int(d3c / 16)
		re = int(d3c % 16)

		if re <= 9:
			hex = str(re) + hex

		elif 9 < re <= 15:
			re = re - 10
			hex = let[re] + hex
		
		d3c = di

	if d3c <= 9:
		print(str(d3c) + hex)

	elif 9 < d3c <= 15:
		h3x = d3c - 10
		print(let[h3x] + hex)
