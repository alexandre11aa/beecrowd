#### Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples, cada treinador coloca um
#### Pomekon na batalha e vence quem tem o Pomekon com maior valor de golpe, que é definido da seguinte maneira: valorgolpe = (ataq
#### ue + defesa)/2 + bonus. O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par. Neste problema será da
#### do a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, c
#### abe a você informar o ganhador da batalha. A entrada é composta por diversas instâncias. A primeira linha da entrada contém um
#### inteiro T indicando o número de instâncias. Cada instância começa com um inteiro B (0 ≤ B ≤ 100), que indica o valor do bônusa
#### plicado. Nas duas linhas seguintes terão três inteiros Ai, Di e Li (1 ≤ Ai, Di ≤ 100, 1 ≤ Li ≤ 50), representado o valor de at
#### aque do Pomekon, o valor de defesa e o level do treinador. A primeira linha representa o Pomekon de Dabriel e a segunda o de G
#### uarte. Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a batalha, em caso de empate imprima:
#### "Empate", sem aspas. Q:2221

qntd = int(input())

for i in range(qntd):
	b = int(input())
	t1 = input().split()
	t2 = input().split()

	if int(t1[2]) % 2 == 0:
		dt1 = (int(t1[0]) + int(t1[1]))/2 + b
	else:
		dt1 = (int(t1[0]) + int(t1[1]))/2

	if int(t2[2]) % 2 == 0:
		dt2 = (int(t2[0]) + int(t2[1]))/2 + b
	else:
		dt2 = (int(t2[0]) + int(t2[1]))/2

	if dt1 > dt2:
		print("Dabriel")
	elif dt1 < dt2:
		print("Guarte")
	else:
		print("Empate")
