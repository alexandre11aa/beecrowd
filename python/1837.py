#### Começou a 4ạ Maratona de Programação da UFFS! Esperamos que você aproveite as próximas horas que passará conosco e que se div
#### irta muito! Boa sorte! Este é o 3ọ ano do Clube de Programação, projeto de extensão que visa em primeiro lugar tornar os prog
#### ramadores da região brasileira conhecida como Fronteira Sul muito mais aptos a enfrentar os desafios computacionais tanto daa
#### cademia quanto do mercado do trabalho. Nossa principal estratégia está em promover oficinas e treinos para competições de Pro
#### gramação, não apenas para estudantes da UFFS, mas para quem quiser participar. Apesar das várias dificuldades, estamos muitof
#### elizes com os resultados que temos conquistado. Em parceria com a UNOCHAPECÓ, a URI e a UNOESC, colaboramos para fazer de Cha
#### pecó nos dois últimos anos a 2ª maior sede do Brasil na etapa regional da Maratona de Programação, o que é mais um indicadord
#### o entusiasmo que o povo daqui tem por Programação. Para aquecer você para esta competição, vamos pedir que você desenvolva um
#### programa que calcule o quociente e o resto da divisão de dois números inteiros, pode ser? Lembre que o quociente e o resto da
#### divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 ≤ r < |b| e: a = b×
#### q + r ; Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como ‘Teorema da
#### Divisão Euclidiana’ ou ‘Algoritmo da Divisão’. A entrada é composta por dois números inteiros a e b (-1.000 ≤ a, b < 1.000).I
#### mprima o quociente q seguido pelo resto r da divisão de a por b. Q:1837

a, b = map(int,input().split())

e = b
    
if b < 0:
	e = b * -1

if a < 0:   
 
	r = 0
	con = True
    
	while con == True:
		f = a - r
		
		if f % b != 0:
			r += 1
            
		if f % b == 0:
			con = False
		
	q = f / b
    
else:
	q = a / b
	r = a % e
	
	if r < 0:
		r *= -1
        
print(int(q),int(r))
