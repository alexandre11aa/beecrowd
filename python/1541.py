#### Sr PI é um construtor muito famoso na cidade de Programolândia. Ele precisa de sua ajuda para encontrar os melhores terrenosd
#### a cidade, para realizar assim a construção de vários projetos de casas que possui. Considere que ele tenha por exemplo, um pr
#### o jeto para construir uma casa de 8 metros por 10 metros, e a legislação do município permite a construção de no máximo 100%d
#### o terreno. Como todos os terrenos nesta cidade são perfeitamente quadrados e o valor dos lados da casa são apenas uma referên
#### cia para a área total a ser construída (80 metros quadrados), o sr PI precisaria de um terreno de 8.994 metros, o que simplif
#### icado daria como resultado 8 metros e o tamanho real da casa seria de 64 metros quadrados. Se a legislação permitisse a utili
#### zar 50% do terreno, o mesmo teria que ter 160 metros para que 50% dele fosse 80 metros quadrados, o suficiente para uma casad
#### e 8 x 8 metros (64 metros quadrados). No primeiro caso de teste, como o percentual para construir é de apenas 20%, o terrenot
#### eria que ter 20 metros de lado para que 1/5 deste terreno tivesse o tamanho de 80 metros quadrados. Ajude o sr PI a determina
#### r o tamanho minimo do terreno. A entrada é composta de vários casos de testes. Cada caso de teste é composto de três númerosi
#### nteiros A, B e C ( > 0 e ≤ 1000) separados por um espaço. Estes números representam as medidas da casa (A e B) e o percentual
#### máximo libera do para construir nesse bairro (C). Um único valor igual a 0 indica o fim das entradas. Você deverá informar um
#### número inteiro, o qual representa a medida do lado do terreno. Este valor deverá ser truncado caso necessário. Q:1541

while True:
	nmr = input()

	if len(nmr) == 1:
		break

	else:
		l1, l2, po = map(int,nmr.split())
		re = int(((l1 * l2 * 100) / po)**(1/2))
		print(re)
