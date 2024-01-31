### Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:  1 x N = N -> 2 x N = 2N ... 10 x N = 10N ; A entradac
### ontém um valor inteiro N (2 < N < 1000). Imprima a tabuada de N, conforme o exemplo fornecido. Q:1078

hh = int(input())

c = 1

for i in range(10):
	tabuada = hh * c
	print("%.f x %.f = %.f" % (c,hh,tabuada))
	c += 1
