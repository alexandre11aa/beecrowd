#### Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras, ele só sabe dar o troco
#### com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, escreva um programa para e
#### le que determine se é possível ou não devolver o troco exato utilizando duas notas. As notas disponíveis são: 2, 5, 10, 20, 50
#### e 100. A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago pelo cli
#### ente (N < M ≤ 104). A entrada termina com N = M = 0. Seu programa deverá imprimir "possible" se for possível devolver o trocoe
#### xato ou "impossible" se não for possível. Q:2140

while True:
	v, n = map(int,input().split())

	if v == n == 0:
		break

	l, c = [[4,7,10,12,15,20,22,25,30,40,52,55,60,70,100,102,105,110,120,150,200], 0]
	
	for i in range(len(l)):
		if (n - v) == l[i]:
			c += 1

	if c == 1:
		print("possible")
	else:
		print("impossible")
