
#### Bem-vindos e bem-vindas à Escola de Inverno da Maratona de Programação 2015 de Erechim! Esperamos sinceramente que vocês apre
#### ndam muito nestes dias para que tenham muito sucesso nas competições de Programação ainda por vir, mas sobretudo esperamos qu
#### e vocês curtam a Escola, pois quando nos divertimos e temos prazer em estudar e programar, o treino deixa de ser um fardo e s
#### e torna um hobby. Então, divirtam-se! O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, pa
#### rticipar de uma roda de chimarrão, assar pinhões no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugareso
#### nde o inverno costuma ser muito cruel. Em Westeros, por exemplo, o humor das pessoas é definido de acordo com as tendências c
#### limáticas. Com base nas temperaturas dos três últimos dias, as pessoas podem ficar tristes ou felizes, ficando mais propensas
#### a fazerguerra ou fazer amor, respectivamente. E, sejamos sinceros, é justamente por causa das cenas de amor e de guerra que a
#### mamos Game of Thrones! Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pes
#### soas ficam felizes (primeira figura). Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º pa
#### ra o 3º, as pessoas ficam tristes (segunda figura). Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu d
#### o 2º para o 3º menos do que subira do 1º para o 2º, as pessoas ficam tristes (terceira figura). Se a temperatura subiu do 1ºp
#### ara o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, as pessoas ficam feli
#### zes (quarta figura). Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que d
#### escera do 1º para o 2º, as pessoas ficam felizes (quinta figura). Se a temperatura desceu do 1º para o 2º dia e do 2º para o3
#### º, mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, as pessoas ficam tristes (sexta figura). Se a te
#### mperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso con
#### trário (respectivamente, sétima e oitava figuras). A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100
#### ), os quais representam respectivamente as temperaturas registradas no 1º, no 2º e no 3º dias. Imprima uma linha contendo uma
#### carinha feliz ou triste, representando como fica o humor do povo de Westeros de acordo com as tendências climáticas. Q:1847

p, s, t = map(int,input().split())

if p < s:
	if (s > t) or (s == t):
		print(":(")
	elif (s < t) and ((s - p) > (t - s)):
		print(":(")
	else:
		print(":)")

if p > s:
	if (t > s) or (t == s):
		print(":)")
	elif (t < s) and((s - t) < (p - s)):
		print(":)")
	else:
		print(":(")

if p == s:
	if t > s:
		print(":)")
	else:
		print(":(")
