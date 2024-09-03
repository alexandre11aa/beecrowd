### Mariazinha quer resolver um problema interessante. Dadas as informações de população e a taxa de crescimento de duas cidades q
### uaisquer (A e B), ela gostaria de saber quantos anos levará para que a cidade menor (sempre é a cidade A) ultrapasse a cidadeB
### em população. Claro que ela quer saber apenas para as cidades cuja taxa de crescimento da cidade A é maior do que a taxa de cr
### escimento da cidade B, portanto, previamente já separou para você apenas os casos de teste que tem a taxa de crescimento maior
### para a cidade A. Sua tarefa é construir um programa que apresente o tempo em anos para cada caso de teste.P orém, em alguns ca
### sos o tempo pode ser muito grande, e Mariazinha não se interessa em saber exatamente o tempo para estes casos. Basta que vocêi
### nforme, nesta situação, a mensagem "Mais de 1 seculo.". A primeira linha da entrada contém um único inteiro T, indicando o núm
### ero de casos de teste (1 ≤ T ≤ 3000). Cada caso de teste contém 4 números: dois inteiros PA e PB (100 ≤ PA < 1000000, PA < PB≤
### 1000000) indicando respectivamente a população de A e B, e dois valores G1 e G2 (0.1 ≤ G1 ≤ 10.0, 0.0 ≤ G2 ≤ 10.0, G2 < G1) co
### m um digito após o ponto decimal cada, indicando respectivamente o crescimento populacional de A e B (em percentual). Atenção:
### A população é sempre um valor inteiro, portanto, um crescimento de 2.5 % sobre uma população de 100 pessoas resultará em 102 p
### essoas, e não 102.5 pessoas, enquanto um crescimento de 2.5% sobre uma população de 1000 pessoas resultará em 1025 pessoas. Al
### ém disso, não utilize variáveis de precisão simples para as taxas de crescimento. Imprima, para cada caso de teste, quantos an
### os levará para que a cidade A ultrapasse a cidade B em número de habitantes. Obs.: se o tempo for mais do que 100 anos o progr
### ama deve apresentara mensagem: Mais de 1 seculo. Neste caso, acredito que seja melhor interromper o programa imediatamente apó
### s passar de 100 anos, caso contrário você poderá receber como resposta da submissão deste problema "Time Limit Exceeded". Q:11
### 60

nmr = int(input())

for i in range(nmr):
	pop1, pop2, per1, per2 = map(float,input().split())
	con1 = 0
    
	while pop1 <= pop2 and con1 <= 100:
		pop1 += int((pop1 * per1 * 0.01))
		pop2 += int((pop2 * per2 * 0.01))
		con1 += 1

	if con1 <= 100:
		print(con1, "anos.")
	else:
		print("Mais de 1 seculo.")
