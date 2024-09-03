#### Números em ponto flutuante podem ser bastante extensos para mostrar. Nesses casos, é conveniente usar a notação científica. Vo
#### cê deve escrever um programa que, dado um número em ponto flutuante, mostre este número na notação científica: sempre mostre o
#### sinal da mantissa; sempre mostre 4 casas decimais na mantissa; use o caractere 'E' para separar a mantissa do expoente; sempre
#### mostre o sinal do expoente; e mostre o expoente com pelo menos 2 dígitos. A entrada é um número em ponto flutuante de dupla pr
#### ecisão X (de acordo com o padrão IEEE 754-2008). Nunca haverá um número com mais de 110 caracteres nem com mais de 6 casas dec
### imais. A saída é o número X em uma única linha na notação científica detalhada acima. Q:1958

nmr = float(input())

c = 0

if nmr <= -10:
	nmr = abs(nmr)
	while nmr >= 10:
		c += 1
		nmr /= 10
	if c < 10:
		print("-{:.4f}E+0{}".format(nmr,c))
	else:
		print("-{:.4f}E+{}".format(nmr,c))

elif -1 > nmr > -10:
	print("-{:.4f}E+00".format(abs(nmr)))

elif 0 > nmr > -1:
	nmr = abs(nmr)
	while nmr < 1:
		c += 1
		nmr *= 10
	if c < 10:
		print("-{:.4f}E-0{}".format(nmr,c))
	else:
		print("-{:.4f}E-{}".format(nmr,c))

elif nmr == 0.0:
	if str(nmr)[0] == "-":
		print("{:.4f}E+00".format(nmr))
	else:
		print("+{:.4f}E+00".format(nmr))
	
elif 1 > nmr > 0:
	while nmr < 1:
		c += 1
		nmr *= 10
	if c < 10:
		print("+{:.4f}E-0{}".format(nmr,c))
	else:
		print("+{:.4f}E-{}".format(nmr,c))	

elif 10 > nmr >= 1:
	print("+{:.4f}E+00".format(nmr))

elif nmr >= 10:
	while nmr >= 10:
		c += 1
		nmr /= 10
	if c < 10:
		print("+{:.4f}E+0{}".format(nmr,c))
	else:
		print("+{:.4f}E+{}".format(nmr,c))
