### Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva uma lgoritmo para
### ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário inform
### e um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerr
### ado quando o código informado for o número 4. A entrada contém apenas valores inteiros e positivos. Deve ser escrito a mensage
### m: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível. Q:1134

con = True
a = 0
g = 0
d = 0

while con == True:
	tipo = int(input())
	if tipo == 1:
		a += 1
	elif tipo == 2:
		g += 1
	elif tipo == 3:
		d += 1
	elif tipo == 4:
		con = False

print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)
