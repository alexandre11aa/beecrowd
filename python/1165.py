### Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é pr
### imo, pois pode ser dividido apenas pelo número 1 e pelo número 7. A entrada contém vários casos de teste. A primeira linha dae
### ntrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes con
### tém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo. Para cada caso de teste de entrada, imprima a mens
### agem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida. Q:1165

con = 1

qntdd = int(input())

while con <= qntdd:

	nmr = float(input())

	if nmr < 0:
		nmr = nmr * -1
    
	divi = nmr - 1

	lgc = True

	while lgc == True and divi >= 1:
		if (nmr % divi == 0) and (divi != 1):
			print("%.i nao eh primo" % nmr)
			lgc = False
		elif divi == 1:
			print("%.i eh primo" % nmr)
		divi = divi - 1
        
	con += 1
