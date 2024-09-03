### Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média
### de todos os valores positivos digitados, com um dígito após o ponto decimal. A entrada contém 6 números que podem ser valoresi
### nteiros ou de ponto flutuante. Pelo menos um destes números será positivo. O primeiro valor de saída é a quantidade de valores
### positivos. A próxima linha deve mostrar a média dos valores positivos digitados. Q:1064

con = 1
num_f = 0
num_p = 0

while con <= 6:
	nmr = float(input())
	if nmr > 0:
		num_f += nmr
		num_p += 1
	con += 1

med = num_f/num_p

print(num_p,"valores positivos")
print("%.1f" % med)
