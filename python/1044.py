### Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicandos
### e os valores lidos são múltiplos entre si. A entrada contém valores inteiros. A saída deve conter uma das mensagens conforme d
### escrito acima. Q:1044

na, nb = input().split()

na = int(na)
nb = int(nb)

if nb > na:
	xx = na
	na = nb
	nb = xx

if (na % nb == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
