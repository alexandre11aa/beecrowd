### Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros Xe
### Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y. A primeira linha de entrada é um inteiro N que é aq
### uantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y. Imprima a
### soma de todos valores ímpares entre X e Y. Q:1099

con = 1
con1 = 1

qtdd = int(input())

while con <= qtdd:
	som = 0
	ni, nf = map(int,input().split())
	if nf < ni:
		xx = nf
		nf = ni
		ni = xx
	nii = ni + 1
	while nii < nf:
		if nii % 2 == 0:
			som += 0
		else:
			som += nii
		nii += 1
	print(som)
	con += 1
