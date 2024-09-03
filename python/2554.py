#### Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha(
#### BH)! Antes de viajar para BH, você e seus N-1 amigos decidiram combinar algum dia para ir a uma pizzaria, para relaxar e desco
#### ntrair (e, naturalmente, comer!). Neste momento está sendo escolhida a data do evento. Para que todas as pessoas possam partic
#### ipar, foi decidido que o encontro na pizzaria ocorrerá em um data tal que todas as N pessoas podem comparecer à pizzaria nesta
#### data. Portanto, nem toda data pode ser escolhida, pois algumas pessoas podem ter outros compromissos já marcados em alguns dia
#### s. Dada a lista de datas consideradas para o evento e a informações de quais pessoas podem comparecer em quais datas, determin
#### e se o evento poderá ocorrer e, em caso positivo, sua data. Caso mais de uma data seja possível, o evento deve ocorrer o maisc
#### edo possível. A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiros N e D (1 ≤ N, D ≤ 50),o
#### número de pessoas e o número de datas consideradas, respectivamente. As pessoas são numeradas de 1 a N. As próximas D linhas d
#### escrevem uma data considerada. Cada linha começa com a data na forma dia∕mes∕ano. A linha é seguida de N inteiros p1,p2,...,pN
#### . O inteiro pi é 1 se a pessoa i pode comparecer na data considerada, ou 0 caso contrário. É garantido que as datas são sempre
#### válidas, e não há zeros à esquerda. Além disso, as datas são dadas em ordem, do dia mais cedo para o dia mais tarde. A entrada
#### termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma linha contendo a data que o evento deve ocorrer, na for
#### ma dia∕mes∕ano, de maneira idêntica à da entrada. Caso não seja possível realizar o evento, imprima “Pizza antes de FdI” (sema
#### spas). Q:2554

while True:
	try:
		co, li = map(int,input().split())

		dias, s_dias, n = [[],[],0]

		for l in range(li):
			dias.append(list(map(str,input().split())))

		for l in range(li):
			nmr = 0
			cnt = 0
			for c in range(co, -1, -1):
				cnt += 1
				nmr += int(dias[l][c])
				if cnt == co:
					break

			s_dias.append(nmr)

		s_dias_c = sorted(s_dias, reverse = True)

		for c in range(len(s_dias_c)):
			if s_dias_c[c] == co:
				n += 1

		if n > 1:
			for l in range(li):
				if s_dias[l] == s_dias_c[0]:
					print(dias[l][0])
					break
		elif n == 1:
			for l in range(li):
				if s_dias[l] == s_dias_c[0]:
					print(dias[l][0])
					break
		else:
			print("Pizza antes de FdI")

	except:
		break
