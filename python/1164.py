### Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (exclui
### ndo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever ump
### rograma que imprima se um determinado número é perfeito ou não. A entrada contém vários casos de teste. A primeira linha da en
### trada contém um inteiro N (1 ≤ N ≤ 20), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes conté
### m um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito. Para cada caso de teste de entrada, imprima a men
### sagem “X eh perfeito” ou “X nao eh perfeito”, de acordo com a especificação fornecida. Q:1164

con = int(input())

for i in range(con):
	nmr = int(input())
	con2 = 1
	soma = 0

	while con2 <= nmr:
		if nmr % con2 == 0:
			soma += con2
		con2 += 1

	if soma - nmr == nmr:
		print(nmr, "eh perfeito")
	else:
		print(nmr, "nao eh perfeito")
