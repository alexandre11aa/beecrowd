### Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. Mostre quantos destesv
### alores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações. A primeira linha da
### entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste. Cada caso de teste a seguir é um valor i
### nteiro X (-107 < X <107). Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do inte
### rvalo. Q:1072

inn = 0
out = 0

ee = int(input())

contad = 0

for i in range(ee):
	ex = int(input())
	if (ex >= 10) and (ex <= 20):
		inn = inn + 1
	else:
		out = out + 1
	contad = contad + 1

print("%.f in" % inn)
print("%.f out" % out)
