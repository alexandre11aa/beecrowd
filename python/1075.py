### Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2. A entrada contému
### m valor inteiro N (N < 10000). Imprima todos valores que quando divididos por N dão resto = 2, um por linha. Q:1075

con = 1

nmr = float(input())

while con <= 10000:
	if con % nmr == 2:
		print(con)
	con += 1
