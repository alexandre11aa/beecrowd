### Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostr
### e a mensagem “divisao impossivel” para os valores em questão. A entrada contém um número inteiro N. Este N será a quantidade d
### e pares de valores inteiros (X e Y) que serão lidos em seguida. Para cada caso mostre o resultado da divisão com um dígito apó
### s o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo. Q:1116

con = 1

nmr = int(input())

while con <= nmr:
	x, y = map(int,input().split())
	if y == 0:
		print("divisao impossivel")
	else:
		divi = x/y
		print(divi)
	con += 1
