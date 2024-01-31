### Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mos
### tre o valor da conta a pagar. O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um
### item conforme tabela acima. O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casasa
### pós o ponto decimal. Q:1038

pa, pb = input().split()

pa = int(pa)
pb = int(pb)

if pa == 1:
	pa = 4
elif pa == 2:
	pa = 4.5
elif pa == 3:
	pa = 5
elif pa == 4:
	pa = 2
else:
	pa = 1.5

conta = pa * pb

print("Total: R$ %.2f" % conta)
