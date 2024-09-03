### Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco ee
### m seguida, os valores na sequência como foram lidos. A entrada contem três números inteiros. Imprima a saída conforme foi espe
### cificado. Q:1042

n1, n2, n3 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

nn1 = n1
nn2 = n2
nn3 = n3

if n1 < n2:
	xx = n1
	n1 = n2
	n2 = xx

if n2 < n3:
	xx = n2
	n2 = n3
	n3 = xx

if n1 < n2:
	xx = n1
	n1 = n2
	n2 = xx

print(n3)
print(n2)
print(n1)
print("")
print(nn1)
print(nn2)
print(nn3)
