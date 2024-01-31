### Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso. A entradac
### ontém um valor inteiro N (5 < N < 2000). Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaix
### o. Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará respost
### a errada. Neste caso, configure a precisão adequadamente para que isso não ocorra. Q:1073

npar = 0

ff = int(input())

for i in range(int(ff/2)):
	npar += 2
	nparel = npar**2
	print("%.f^2 = %.f" % (npar,nparel))
