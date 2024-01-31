#### No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qu
#### al dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do impasse é uma disputa
#### de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas deP
#### edra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock. As regras do jogo proposto são: at
#### esoura corta o papel; o papel embrulha a pedra; a pedra esmaga o lagarto; o lagarto envenena Spock; Spock destrói a tesoura;a
#### tesoura decapita o lagarto; o lagarto come o papel; o papel contesta Spock; Spock vaporiza a pedra; a pedra quebra a tesoura.
#### Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não é difıcil deduzir o que aco
#### nteceria se a disputa continuasse. Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj ve
#### ncesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". Conhecidas
#### as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon. Q:1828

con = int(input())

nmr = 1

while nmr <= con:
	s, r = input().split()
	
	if s == r:
		print("Caso #%.i: De novo!" % nmr)

	if s == "pedra":
		if r == "tesoura":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "lagarto":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "papel":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "Spock":
			print("Caso #%.i: Raj trapaceou!" % nmr)

	if s == "papel":
		if r == "tesoura":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "lagarto":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "pedra":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "Spock":
			print("Caso #%.i: Bazinga!" % nmr)

	if s == "tesoura":
		if r == "papel":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "lagarto":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "pedra":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "Spock":
			print("Caso #%.i: Raj trapaceou!" % nmr)

	if s == "lagarto":
		if r == "papel":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "tesoura":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "pedra":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "Spock":
			print("Caso #%.i: Bazinga!" % nmr)

	if s == "Spock":
		if r == "papel":
			print("Caso #%.i: Raj trapaceou!" % nmr)
		elif r == "tesoura":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "pedra":
			print("Caso #%.i: Bazinga!" % nmr)
		elif r == "lagarto":
			print("Caso #%.i: Raj trapaceou!" % nmr)

	nmr += 1
