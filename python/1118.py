### Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O pr
### ograma só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separ
### adamente. No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1o
### u 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o códi
### go 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerra
### do. O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve serl
### ido um valor inteiro X . O programa deve parar quando o valor lido para este X for igual a 2. Se uma nota inválida for lida, d
### eve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” se
### guido do valor do cálculo. Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem dev
### e ser apresentada novamente se o valor da entrada padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaix
### o. A média deve ser impressa com dois dígitos após o ponto decimal. Q:1118

con1 = True

while con1 == True:

	soma = 0
	con = 1

	while con <= 2:
		nota = float(input())
		if nota < 0 or nota > 10:
			print("nota invalida")
		else:
			soma += nota
			con += 1

	media = soma/2
	print("media = %.2f" % media)
	print("novo calculo (1-sim 2-nao)")
	con2 = True

	while con2 == True:
		decisao = float(input())
		if decisao != 1 and decisao != 2:
			print("novo calculo (1-sim 2-nao)")
		elif decisao == 1:
			con2 = False
		else:
			con1 = False
			con2 = False
