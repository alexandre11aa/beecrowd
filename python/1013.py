### Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a f
### órmula: MaiorAB = (a + b + abs(a-b)/2 ; Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo pass
### o, portanto é necessário para chegar no resultado esperado. O arquivo de entrada contém três valores inteiros. Imprima o maiord
### os três valores seguido por um espaço e a mensagem "eh o maior". Q:1013

av, bv, cv = input().split()

av = int(av)
bv = int(bv)
cv = int(cv)

if bv > av:
	xx = av
	av = bv
	bv = xx

if cv > bv:
	xx = bv
	bv = cv
	cv = xx

if bv > av:
	xx = av
	av = bv
	bv = xx

print("%.f eh o maior" % av)
