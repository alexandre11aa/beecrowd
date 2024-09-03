### Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A segu
### ir, mostre a quantidade de valores positivos digitados. Seis valores, negativos e/ou positivos. Imprima uma mensagem dizendo qu
### antos valores positivos foram lidos. Q:1060

maize = 0

for i in range(6):
	aa = float(input())
	if aa > 0:
		maize = maize + 1
	else:
		maize = maize + 0
print(maize,"valores positivos")
