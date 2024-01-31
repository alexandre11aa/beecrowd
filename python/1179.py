### Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tama
### nho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o v
### etor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que res
### tou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes qu
### antas for necessário. A entrada contém 15 números inteiros. Imprima a saída conforme o exemplo abaixo. Q:1179

par = []
impar = []

for i in range(15):
	nmr = float(input())
	if nmr % 2 == 0:
		par.append(nmr)
	elif nmr % 2 != 0:
		impar.append(nmr)
		
	if len(par) == 5:
		for j in range(5):
			print("par[%.f] = %.f" % (j,par[j]))
		par = []
	elif len(impar) == 5:
		for k in range(5):
			print("impar[%.f] = %.f" % (k,impar[k]))
		impar = []

for m in range(len(impar)):
	print("impar[%.f] = %.f" % (m,impar[m]))

for n in range(len(par)):
	print("par[%.f] = %.f" % (n,par[n]))
