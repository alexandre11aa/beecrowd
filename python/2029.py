#### Seu Júlio é proprietário de um grande apiário situado no interior da Paraíba. Todo ano, semestralmente, seu Júlio coleta o mel
#### produzido pelas abelhas da sua propriedade e armazena-o em um recipiente de formato CILÍNDRICO para que facilite o transported
#### o mel para os estabelecimentos que encomendam esse produto natural para a comercialização. Certa vez seu Júlio percebeu que de
#### vido a um crescimento na produção do mel, em relação ao semestre anterior, o recipiente que possuia não suportaria o volume de
#### mel produzido por suas abelhas. Seu Júlio precisa agora que você faça um programa que informado o volume de mel em cm3 e o diâ
#### metro da parte interna do recipiente em cm, calcule e mostre: - Qual deve ser a altura(em cm) da parte interna do recipiente;-
#### A área(em cm2) da boca(entrada) do recipiente. Obs.: Considere π = 3.14 | A entrada contém vários casos de teste e termina com
#### EOF. Cada caso de teste consiste de duas linhas contendo em cada uma um valor de ponto flutuante de dupla precisão com duas ca
#### sas decimais após a vírgula, sendo um V (1.00 ≤ V ≤ 10000.00) e outro D (1.00 ≤ D ≤ 100.00), representando respectivamente o v
#### olume e o diâmetro do recipiente. Para cada teste, a saída contém na primeira linha a mensagem "ALTURA = ", com um espaço depo
#### is de ALTURA e outro depois do símbolo de igualdade, seguido do valor da altura do recipiente com duas casas decimais após a v
#### írgula e na segunda linha a mensagem "AREA = ", também com um espaço depois de AREA e outro depois do símbolo de igualdade, se
#### guido do valor da area da boca(entrada) do recipiente com duas casas decimais após a vírgula. - Não esqueça da quebra de linha
#### ao final da saída,caso contrário você receberá "Presentation Error". Q:2029

while True:
	try:
		v = float(input())
		d = float(input())

		a = 3.14 * (d/2)**2
		h = v/a		

		print("ALTURA = %.2f" % h)
		print("AREA = %.2f" % a)

	except EOFError:
		break
