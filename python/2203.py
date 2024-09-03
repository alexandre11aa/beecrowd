#### Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", ela funcionad
#### a seguinte maneira: Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma dire
#### ção até uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele ressu
#### rge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano. Fiddlesticks quer sua aju
#### da para saber se de uma certa posição é possível atingir um invasor com sua habilidade ultimate. Obs: Considere que Fiddlestic
#### ks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na direção contrária a Fiddlesticks, em velocid
#### ade constante. A entrada é composta de várias linhas, cada linha contém os seguintes valores inteiros: Xf, Yf, Xi, Yi, Vi, R1e
#### R2(0 ≤ Xf, Yf, Xi, Yi, Vi, R1 e R2 ≤ 100), representando respectivamente as coordenadas de Fiddlesticks, as coordenadas inicia
#### is do invasor, a velocidade do invasor, o raio de conjuração da ultimate e o raio de voo dos corvos. Considere a unidade de me
#### dida como sendo o metro. Na saída você deve imprimir para cada linha o caractere 'Y' caso seja possível atingir o invasor ou '
#### N' caso contrário, ambos seguidos de uma quebra de linha. Q:2203

while True:
	try:
		xf, yf, xi, yi, vi, r1, r2 = map(int,input().split())

		dif = ((xi - xf)**2 + (yi - yf)**2)**(1/2)  
		dif += (vi * 1.5)
		r = r1 + r2

		if dif > float(r):
			print("N")
		else:
			print("Y")
		
	except:
		break
