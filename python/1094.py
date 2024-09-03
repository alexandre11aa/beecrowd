### Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentosd
### e um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o
### percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelho
### s. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada
### e a quantidade de cobaias utilizadas em cada experimento. A primeira linha de entrada contém um valor inteiro N que indica osv
### ários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quanti
### dade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho). Apresen
### te o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de c
### obaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto. Q:1094

con = 1
cot = 0
coc = 0
cor = 0
cos = 0

nmr = int(input())

while con <= nmr:
	qntdd, cobaia = input().split()
	qntdd = float(qntdd)
	cot += qntdd
	if cobaia == "C":
		coc += qntdd
	if cobaia == "R":
		cor += qntdd
	if cobaia == "S":
		cos += qntdd
	con += 1

pec = (coc*100)/cot
per = (cor*100)/cot
pes = (cos*100)/cot
	
print("Total: %.f cobaias" % cot)
print("Total de coelhos: %.f" % coc)
print("Total de ratos: %.f" % cor)
print("Total de sapos: %.f" % cos)
print("Percentual de coelhos: {0:.2f} %".format(pec))
print("Percentual de ratos: {0:.2f} %".format(per))
print("Percentual de sapos: {0:.2f} %".format(pes))
