#### O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve ump
#### roblema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moçad
#### o caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um p
#### rograma para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu re
#### spectivo valor. 1001 | R$ 1.50 - 1002 | R$ 2.50 - 1003 | R$ 3.50 - 1004 | R$ 4.50 - 1005 | R$ 5.50 . A primeira entrada inform
#### ada é a quantidade de produtos comprados (1 <= p <= 5). Para cada produto segue a quantidade (1 <= q <= 500) que o consumidorc
#### omprou. Obs.: não poderão ser informados números de produtos repetidos. Você deve imprimir o valor da compra com duas casas de
#### cimais. Q:1985

n = int(input())

l = [1.5,2.5,3.5,4.5,5.5]
s = 0

for i in range(n):
	lan, qtd = map(int,input().split())
	s += (l[lan - 1001] * qtd)

print("%.2f" % s)
