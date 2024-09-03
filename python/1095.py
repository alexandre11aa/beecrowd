### Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo. Não há nenhuma entrada neste problema. Imprim
### a a sequencia conforme exemplo abaixo: I=1 J=60 / I=4 J=55 / I=7 J=50 / ... / I=? J=0. Um abaixo do outro. Q:1095

j = 60
i = 1

while j >= 0:
	print("I=%.f J=%.f" % (i,j))
	j -= 5
	i += 3
