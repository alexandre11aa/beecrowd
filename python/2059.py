#### Um novo jogo chamado Ímpar, Par ou Roubo (IPR) está se tornando muito popular. Esse jogo surgiu quando alguns amigos estavam s
#### em conexão com a internet, sem celular, sem computador e bastante desocupados. O jogo está tão popular que irá acontecer um ca
#### mpeonato mundial de IPR e cada país do mundo irá escolher um representante para competir. O jogo funciona da seguinte forma: d
#### ois jogadores participam, o jogador 1 escolhe entre par ou ímpar, então cada jogador escolhe um inteiro positivo, se a soma de
#### sses números for par e o jogador 1 tiver escolhido par então o jogador 1 ganha, se a soma for ímpar o jogador 2 ganha. Caso oj
#### ogador 1 tivesse escolhido ímpar ele ganharia se a soma fosse ímpar, caso a soma fosse par o jogador 2 ganharia. Nada de difer
#### ente de um jogo de par ou ímpar convencional, correto? A diferença do jogo é que o jogador 1 pode roubar e assim assegurar sua
#### vitória independentemente do resultado do jogo de ímpar ou par convencional, já o jogador 2 pode ou não acusar o jogador 1 der
#### oubo. Com essas adições no jogo se o jogador 1 roubar e o jogador 2 acusar o roubo então o jogador 2 ganha, caso o jogador 2 n
#### ão acuse o roubo e o jogador 1 roubar então o jogador 1 ganha, caso o jogador 2 acuse o roubo, mas o jogador 1 não tiver rouba
#### do então o jogador 1 ganha, se o jogador 1 não roubar e o jogador 2 não acusar o roubo o jogo segue como descrito anteriorment
#### e. Você foi contratado pela OIIPR (Organização Internacional de Ímpar, Par ou Roubo) para desenvolver um programa que dada a e
#### scolha do jogador 1 entre par ou ímpar, os números escolhidos como jogada e as ações dos jogadores (roubo/acusação) mostre que
#### m foi o vencedor. A entrada consite de uma única linha contendo 5 inteiros: p, j1, j2, r, a. ( 0 ≤ p, r, a ≤ 1 e 1 ≤ j1, j2 ≤1
#### 00). p representa a escolha do jogador 1 (se p = 1 então o jogador 1 escolheu par, se p = 0 então o jogador 1 escolheu ímpar).
#### Os valores j1, j2, representam respectivamente o número escolhido pelo jogador 1 e pelo jogador 2. r representa se o jogador 1
#### roubou (se r = 1 então o jogador 1 roubou, se r = 0 então o jogador 1 não roubou), a representa se o jogador 2 acusou o roubo(
#### se a = 1 então o jogador 2 acusou o jogador 1 de roubo, se a = 0 então ele não acusou o jogador 1 de roubo). Imprima "Jogador1
#### ganha!" se o jogador 1 ganhou ou "Jogador 2 ganha!" se o jogador 2 ganhou (sem as aspas). Q:2059

p, j1, j2, r, a = map(int,input().split())

if r == 1 and a == 1:
	print("Jogador 2 ganha!")

elif r == 1 and a == 0:
	print("Jogador 1 ganha!")

elif r == 0 and a == 1:
	print("Jogador 1 ganha!")

elif p == 1:
	if (j1 + j2) % 2 == 0:
		print("Jogador 1 ganha!")
	else:
		print("Jogador 2 ganha!")

elif p == 0:
	if (j1 + j2) % 2 == 0:
		print("Jogador 2 ganha!")
	else:
		print("Jogador 1 ganha!")
