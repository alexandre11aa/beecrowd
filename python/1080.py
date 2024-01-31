### Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos. O arquivo de entrada co
### ntém 100 números inteiros, positivos e distintos. Apresente o maior valor lido e a posição de entrada. Q:1080

con = 1
n_ma = 1
pos = 1

while con <= 100:
	nmr = int(input())
	if nmr > n_ma:
		n_ma = nmr
		pos = con
	con += 1 

print(n_ma)
print(pos)
