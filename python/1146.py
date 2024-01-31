### Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero
### ). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor. Obs: cuide para não de
### ixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error. O arquivo de entrada conté
### m vários números inteiros. O último número no arquivo de entrada é 0. Para cada número N do arquivo de entrada deve ser impres
### sa uma linha de 1 até N, conforme o exemplo abaixo. Não deve haver espaço em branco após o último valor da linha. Q:1146

con = True

while con == True:
	inf = ""
	con1 = 1
	nmr = int(input())
	if nmr != 0:
		while con1 <= nmr:
			if con1 < nmr:
				inf += str(con1) + " "
				con1 += 1
			else:
				inf += str(con1)
				con1 += 1
		print(inf)
	else:
		con = False
