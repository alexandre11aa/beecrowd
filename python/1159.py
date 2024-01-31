### O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cadaX
### lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exem
### plo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a
### saída deve ser 80, que é a soma de 12+14+16+18+20. O arquivo de entrada contém muitos valores inteiros. O último valor do arqu
### ivo é zero. Imprima a saida conforme a explicação acima e o exemplo abaixo. Q:1159
		
con = True

while con == True:
	nmr = int(input())
	soma = 0
	con1 = nmr
	if nmr == 0:
		con = False
	else:
		for j in range(10):
			if con1 % 2 == 0:
				soma += con1
			con1 += 1
		print(soma)
