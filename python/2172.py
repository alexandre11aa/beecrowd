#### Prog e Cackto começaram recentemente a jogar um jogo de RPG chamado Fortaleza. Neste, para o jogador evoluir de nível o mesmop
#### recisa derrotar monstros, nos quais dá um valor de experiência (XP) para o jogador. A produtora do jogo, Jogos Extremos, anunc
#### iou que na próxima semana irá realizar o primeiro evento XP no qual aumentará a experiência dos monstros em X vezes. Como Prog
#### e Cackto estão em um nível muito alto no qual os monstros tem um valor muito alto de pontos de experiência, eles estão tendo d
#### ificuldades de calcular a quantidade de pontos de experiência que os monstros terão durante o evento. Você pode ajudá-los? Hav
#### erá diversos casos de teste. Cada caso de teste contém dois valores X (0 < X ≤ 3) indicando o valor de aumento da EXP dos mons
#### tros e M (10 ≤ M ≤ 232-1) indicando o valor de EXP do monstro. A entrada termina com os valores X == 0 e M == 0, nos quais não
#### devem ser processados. Para cada caso, seu programa deverá mostrar um valor E, referente ao novo EXP do monstro. Q:2172

while True:
	m, x = map(int,input().split())

	if m == 0 and x == 0:
		break

	print(m * x)
