### Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não
### entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos. A entrada
### contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido. A saída contém um valo
### r correspondente à média de idade dos indivíduos. A média deve ser impressa com dois dígitos após o ponto decimal. Q:1154

con = True

ba = 0
ci = 0

while con == True:
	n = float(input())
	if n >= 0:
		ba += 1
		ci += n
	else:
		con = False

media = ci/ba

print("%.2f" % media)
