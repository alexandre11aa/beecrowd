#### Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativasd
#### e saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram suces
#### so (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram suc
#### esso. A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores. Abaixo do nome de
#### cada jogador, seguem duas linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam a quantida
#### de de tentativas de saques, bloqueios e ataques e na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o núm
#### ero de saques, bloqueios e ataques deste jogador que tiveram sucesso. A saída deve conter o percentual total de saques, bloque
#### ios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo. Q:2310

qntd = int(input())

st, bt, at, sa, ba, aa = [0,0,0,0,0,0]
 
for i in range(qntd):
	nome = input()
	t = list(map(float,input().split()))
	a = list(map(float,input().split()))

	st += t[0]
	bt += t[1]
	at += t[2]
	sa += a[0]
	ba += a[1]
	aa += a[2]

print("Pontos de Saque: {:.2f} %.".format((sa/st) * 100))
print("Pontos de Bloqueio: {:.2f} %.".format((ba/bt) * 100))
print("Pontos de Ataque: {:.2f} %.".format((aa/at) * 100))
