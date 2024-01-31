### Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo. Não há nenhuma entrada neste problema. Imprim
### a a sequencia conforme exemplo abaixo. I=0 J=1 / I=0 J=2 / I=0 J=3 / I=0.2 J=1.2 / I=0.2 J=2.2 / I=0.2 J=3.2 / ..... / I=2 J=?
### / I=2 J=? / I=2 J=?. Um abaixo do outro. Q:1098

i = 0
j1 = 1
j2 = 2
j3 = 3

while i < 1:
	if i == 0:
		print("I=%.f J=%.f" % (i,j1))
		print("I=%.f J=%.f" % (i,j2))	
		print("I=%.f J=%.f" % (i,j3))
	else:
		print("I=%.1f J=%.1f" % (i,j1))
		print("I=%.1f J=%.1f" % (i,j2))	
		print("I=%.1f J=%.1f" % (i,j3))
	i += 0.2
	j1 += 0.2
	j2 += 0.2
	j3 += 0.2

while i < 1.8:
	if i == 1:
		print("I=%.f J=%.f" % (i,j1))
		print("I=%.f J=%.f" % (i,j2))	
		print("I=%.f J=%.f" % (i,j3))
	else:
		print("I=%.1f J=%.1f" % (i,j1))
		print("I=%.1f J=%.1f" % (i,j2))	
		print("I=%.1f J=%.1f" % (i,j3))
	i += 0.2
	j1 += 0.2
	j2 += 0.2
	j3 += 0.2

i += 0.2
j1 += 0.2
j2 += 0.2
j3 += 0.2

print("I=%.f J=%.f" % (i,j1))
print("I=%.f J=%.f" % (i,j2))	
print("I=%.f J=%.f" % (i,j3))
