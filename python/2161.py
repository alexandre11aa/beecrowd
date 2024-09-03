#### Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse métodou
#### sa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes. Por exemplo, a
#### o repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10. Sua tarefa é, dado o número N de repetições, calcul
#### ar o valor aproximado da raiz quadrada de 10. A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições
#### do denominador na fração continuada. A saída é o valor aproximado da raiz quadrada com 10 casas decimais. Q:2161

qntd = int(input())

fra = 1/6

for i in range(qntd - 1):
	fra = 1/(6 + fra)

if qntd == 0:
	print("%.10f" % 3)
else:
	print("%.10f" % (3 + fra))
