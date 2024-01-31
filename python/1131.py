### A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENA
### IS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensage
### m "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicita
### ndo o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo: - Quantos GRENAIS
### fizeram parte da estatística. / - O número de vitórias do Inter. / - O número de vitórias do Grêmio. / - O número de Empates./
### - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado). Oa
### rquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em se
### guida háverá um inteir o (1 ou 2), correspondente à repetição do programa. Após cada leitura dos gols, deve ser impressa a men
### sagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição a
### presentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo. Q:1131

con = True
vi = 0
vg = 0
e = 0
qnt = 0

while con == True:
	i, g = map(int,input().split())
	if i > g:
		vi += 1
	elif g > i:
		vg += 1
	else:
		e += 1
	
	qnt += 1
	con1 = True
	print("Novo grenal (1-sim 2-nao)")

	while con1 == True:
		novo = int(input())
		if novo != 1 and novo != 2:
			print("Novo grenal (1-sim 2-nao)")
		elif novo == 1:
			con1 = False
		else:
			con = False
			con1 = False

print(qnt,"grenais")
print("Inter:%.f" % vi) 
print("Gremio:%.f" % vg)
print("Empates:%.f" % e)

if vi > vg:
	print("Inter venceu mais")
elif vi < vg:
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")
