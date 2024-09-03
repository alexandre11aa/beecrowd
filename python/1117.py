### Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com qu
### e o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separa
### damente. A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duasn
### otas válidas. Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida". Quando duas notas válidas forem li
### das, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o p
### onto decimal. Q:1117

con = 1
soma = 0

while con <= 2:
	nota = float(input())
	if nota < 0 or nota > 10:
		print("nota invalida")
	else:
		soma += nota
		con += 1
media = soma/2
print("media = %.2f" % media)
