### Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a ca
### da X números. O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000). Cada sequência deve ser impr
### essa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco a
### pós o último valor da linha. Q:1145

con = True

n1, n2 = map(int,input().split())

nn1 = n2
nnn1 = n1
con2 = 1

while con == True:
	con1 = 1
	nn1 -= n1
	conc = ""
    
	if nn1 > 0:
		while con1 <= nnn1:
			if con1 < nnn1:
		        	conc += str(con2) + " "
		        	con1 += 1
		        	con2 += 1
			else:
		        	conc += str(con2)
		        	con1 += 1
		        	con2 += 1				
		print(conc)
	    
	elif nn1 < 0:
		nnn1 = nn1 + n1
		while con1 <= nnn1:
			if con1 < nnn1:
		        	conc += str(con2) + " "
		        	con1 += 1
		        	con2 += 1
			else:
		        	conc += str(con2)
		        	con1 += 1
		        	con2 += 1
				con = False
		print(conc)
            
	elif nn1 == 0:
		while con1 <= nnn1:
			if con1 < nnn1:
		        	conc += str(con2) + " "
		        	con1 += 1
		        	con2 += 1
			else:
		        	conc += str(con2)
		        	con1 += 1
		        	con2 += 1
				con = False
		print(conc)
