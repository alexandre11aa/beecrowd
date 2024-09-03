### Faça um programa que leia dois inteiros: X e Z (devem ser lidos tantos valores para Z quantos necessários, até que seja digita
### do um valor maior do que X para ele). Conte quantos números inteiros devem ser somados em sequência (considerando o X nesta so
### ma) para que a soma ultrapasse a Z o mínimo possível. Escreva o valor final da contagem. A entrada pode conter, por exemplo, o
### s valores 21 21 15 30. Neste caso, é então assumido o valor 21 para X enquanto os valores 21 e 15 devem ser desconsiderados po
### is são menores ou iguais a X. Como o valor 30 está dentro da especificação (maior do que X) ele será válido e então deve-se pr
### ocessar os cálculos para apresentar na saída o valor 2, pois é a quantidade de valores somados para se produzir um valor maior
### doque 30 (21 + 22). A entrada contém somente valores inteiros, um por linha, podendo ser positivos ou negativos. O primeiro va
### lor da entrada será o valor de X. A próxima linha da entrada irá conter Z. Se Z não atendera especificação do problema, ele de
### verá ser lido novamente, tantas vezes quantas forem necessárias. Imprima um a linha com um número inteiro que representa a qua
### ntidade de números inteiros que devem ser somadas, de acordo com a especificação acima. Q:1150
	
x = int(input())
z = 0

con = True

while con == True:
	cz = int(input())
	if cz > x:
		z = cz
		con = False

nvezes = 0
con2 = x
cx = x

while z >= con2:
	cx += 1
	con2 += cx
	nvezes += 1

nvezes += 1

print(nvezes)
