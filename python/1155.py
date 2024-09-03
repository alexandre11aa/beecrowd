### Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula: S = 1 + 1/2 + 1/3 + … + 1/100. Não há n
### enhuma entrada neste problema. A saída contém um valor correspondente ao valor de S. O valor deve ser impresso com dois dígito
### s após o ponto decimal. Q:1155

x = 100
s = 0

for i in range(100):

	s += 1/x
	x -= 1

print("%.2f" % s)
