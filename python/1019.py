### Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no fo
### rmato horas:minutos:segundos. O arquivo de entrada contém um valor inteiro N. Imprima o tempo lido no arquivo de entrada (segun
### dos), convertido para horas:minutos:segundos, conforme exemplo fornecido. Q:1019

temp = int(input())

if temp > 3600:
	hor = temp/3600
	min = (temp % 3600)/60
	seg = (temp % 3600) % 60
	print("%.i:%.i:%.i" % (hor,min,seg))
else:
	min = temp/60
	seg = temp % 60
	print("0:%.i:%.i" % (min,seg))
