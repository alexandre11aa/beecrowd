### Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo. Não há nenhuma entrada neste problema. Imprim
### a a sequencia conforme exemplo abaixo. I=1 J=7 / I=1 J=6 / I=1 J=5 / I=3 J=9 / I=3 J=8 / I=3 J=7 /  ...  / I=9 J=15 / I=9 J=14
### / I=9 J=13. Um abaixo do outro. Q:1097

i = 1
j1 = 7
j2 = 6
j3 = 5

while i <= 9:
	print("I=%.f J=%.f" % (i,j1))
	print("I=%.f J=%.f" % (i,j2))	
	print("I=%.f J=%.f" % (i,j3))
	i += 2
	j1 += 2
	j2 += 2
	j3 += 2
