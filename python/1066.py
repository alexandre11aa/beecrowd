### Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quant
### os valores digitados foram positivos e quantos valores digitados foram negativos. O arquivo de entrada contém 5 valores inteir
### os quaisquer. Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após ca
### da uma. Q:1066

cont = 1
maiorze = 0
menorze = 0
par = 0
impar = 0

while cont <= 5:
	bb = float(input())
	cont = cont + 1
	if bb > 0:
		maiorze = maiorze + 1
	elif bb < 0:
		menorze = menorze + 1
	else:
		maiorze = maiorze + 0
		menorze = menorze + 0
	
	if bb % 2 == 0:
		par = par + 1
	else:
		impar = impar + 1

print("%.f valor(es) par(es)" % par)
print("%.f valor(es) impar(es)" % impar)
print("%.f valor(es) positivo(s)" % maiorze)
print("%.f valor(es) negativo(s)" % menorze)
