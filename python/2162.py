#### Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatament
#### e na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seg
#### uido por outro pico, nem um vale seguido por outro vale. O professor MC ficou curioso com esse padrão e quer saber se, ao medi
#### r outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não. A entrada é dad
#### a em duas linhas. A primeira tem o número N de medidas da paisagem (1 < N ≤ 100). A segunda linha tem N inteiros: a altura Hid
#### e cada medida (-10000 ≤ Hi ≤ 10000, para todo Hi, tal que 1 ≤ i ≤ N). Uma medida é considerada um pico se é maior que a medida
#### anterior. Uma medida é considerada um vale se é menor que a medida anterior. A saída é dada em uma única linha. Caso a paisage
#### m tenha o mesmo padrão da Nlogônia, deve ser mostrado o número 1. Caso contrário, mostra-se o número 0. Q:2162

tip = 1

qnt = int(input())
nmr = list(map(int,input().split()))

if nmr[0] > nmr[1]:
	for i in range(qnt):
		if i < len(nmr) - 1: 
			if i % 2 == 0:
				if nmr[i] <= nmr[i + 1]:
					tip = 0
			else:
				if nmr[i] >= nmr[i + 1]:
					tip = 0
else:
	for i in range(qnt):
		if i < len(nmr) - 1: 
			if i % 2 == 0:
				if nmr[i] >= nmr[i + 1]:
					tip = 0
			else:
				if nmr[i] <= nmr[i + 1]:
					tip = 0

print(tip)
