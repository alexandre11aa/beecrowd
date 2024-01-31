#### Paulo e Pedro fizeram uma longa jornada desde que partiram do Brasil para competir na Final Mundial da Maratona, em Phuket, Ta
#### ilândia. Notaram que a cada escala que faziam, tinham que ajustar seus relógios por causa do fuso horário. Assim, para melhors
#### e organizarem para as próximas viagens, eles pediram que você faça um aplicativo para celular que, dada a hora de saída, tempo
#### de viagem e o fuso do destino com relação à origem, você informe a hora de chegada de cada vôo no destino. Por exemplo, se ele
#### s partiram às 10 horas da manhã para uma viagem de 4 horas rumo a um destino que fica à leste, em um fuso horário com uma hora
#### a mais com relação ao fuso horário do ponto de partida, a hora de chegada terá que ser: 10 horas + 4 horas de viagem + 1 horad
#### e deslocamento pelo fuso, ou seja, chegarão às 15 horas. Note que se a hora calculada for igual a 24, seu programa deverá impr
#### imir 0 (zero). A entrada contém 3 inteiros: S (0 ≤ S ≤ 23), T (1 ≤ T ≤ 12) e F (-5 ≤ F ≤ 5), separados por um espaço, indicand
#### o respectivamente a hora da saída, o tempo de viagem e o fuso horário do destino com relação à origem. Imprima um inteiro quei
#### ndica a hora local prevista no destino, conforme os exemplos abaixo. Q:2057

sai, tmp, chg = map(int,input().split())

for i in range(tmp):
	sai += 1

	if sai == 24:
		sai = 0

if chg < 0:
	for i in range(chg * -1):
		sai -= 1
	
		if sai == -1:
			sai = 23
else:
	for i in range(chg):
		sai += 1

		if sai == 24:
			sai = 0

print(sai)
