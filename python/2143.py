#### Todo ano após a competição que ocorre na cidade de Taxilândia, os participantes e os coaches vão para o célebre restaurante Ra
#### dar. Porém, os garçons (sempre muito gentis e educados) ficam sobrecarregados devido à quantidade de pessoas, e consequentemen
#### te, acabam demorando um pouco para atender a um pedido. Os participantes ou coaches que sentam nas pontas são os privilegiados
#### , pois são atendidos com somente um pedido, mas os demais precisam sempre pedir duas vezes, pois os garçons (apesar de gentise
#### educados) são desatentos e se esquecem facilmente dos pedidos. Além disso, há uma superstição entre os participantes e coaches
#### de que se não houver um número par de pessoas que não sentam nas pontas, na próxima competição nenhuma equipe da universidadec
#### onseguirá vencer. Portanto, sua tarefa é determinar a soma da quantidade de pedidos de cada um para saber se vale a pena ir ao
#### Radar. Mas apesar do resultado, lembre-se: sempre vale a pena ir ao Radar! A entrada é composta por T (1 ≤ T ≤ 100) indicandoa
#### quantidade de casos de teste e então, T inteiros N (3 ≤ N ≤ 104), indicando a quantidade de pessoas. A mesa é retangular e hav
#### erá pelo menos e no máximo uma pessoa em uma das pontas, isto é, se uma ponta estiver vazia, a outra deve ser ocupada, ou senã
#### o, as duas pontas estarão ocupadas, mas o número de pessoas que não estão nas pontas sempre será par. O final da entrada é ind
#### icado por T = 0. Seu programa deverá imprimir a soma da quantidade de pedidos de cada pessoa. Não haverá linha em branco entre
#### os casos de teste. Q:2143

while True:

	qntd = int(input())

	l = []
		
	if qntd == 0:
		break

	for i in range(qntd):
		pedd = int(input())
		if pedd % 2 != 0:
			l.append(pedd * 2 - 1)
		else:
			l.append(pedd * 2 - 2)

	for i in range(qntd):
		print(l[i])
