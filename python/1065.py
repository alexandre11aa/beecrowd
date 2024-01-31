### Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação. O arq
### uivo de entrada contém 5 valores inteiros quaisquer. Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade d
### e valores pares lidos. Q:1065

con = 1
num_p = 0

while con <= 5:
	nmr = float(input())
	if nmr % 2 == 0:
		num_p += 1
	con += 1

print(num_p,"valores pares")
