#### Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse métodou
#### sa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes. Por exemplo, a
#### o repetir 2 vezes a fração continuada para calcular a raiz quadrada de 2. Sua tarefa é, dado o número N de repetições, calcula
#### r o valor aproximado da raiz quadrada de 2. A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições d
#### o denominador na fração continuada. A saída é o valor aproximado da raiz quadrada com 10 casas decimais. Q:2166

qnt = int(input())

fra = 1/2

for i in range(qnt - 1):
	fra = 1/(2 + fra)

if qnt == 0:
	print("1.0000000000")
else:
	print("%.10f" % (1 + fra))
