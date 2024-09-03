### Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula: S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/? Nã
### o há nenhuma entrada neste problema. A saída contém um valor correspondente ao valor de S. O valor deve ser impresso com doisd
### ígitos após o ponto decimal. Q:1156

s1 = 1
s2 = 1
st = 0

for i in range(19):

	st += s1/s2
	s1 += 2
	s2 *= 2

print("%.2f" % st)
