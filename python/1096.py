### Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo. Não há nenhuma entrada neste problema. Imprim
### a a sequencia conforme exemplo abaixo: I=1 J=7 / I=1 J=6 / I=1 J=5 / I=3 J=7 / I=3 J=6 / I=3 J=5 /  ...  / I=9 J=7 / I=9 J=6 /
### I=9 J=5. Um abaixo do outro. Q:1096

i = 1

while i <= 9:
	print("I=%.f J=7" % i)
	print("I=%.f J=6" % i)	
	print("I=%.f J=5" % i)
	i += 2
