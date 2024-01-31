### Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeir
### os elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonac
### ci calculados neste problema devem caber em um inteiro de 64 bits sem sinal. A primeira linha da entrada contém um inteiro T,i
### ndicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo term
### o da série de Fibonacci. Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da séri
### e de Fibonacci. Q:1176

v = [0,1]

fib = 1
num = 0

for i in range(3,64):

	fib += num
	num = fib - num
	v.append(fib)

nmr = int(input())

for j in range(nmr):
	nmr1 = int(input())
	print("Fib(%.f) = %.f" % (nmr1,v[nmr1]))
