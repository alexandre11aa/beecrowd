### Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pert
### ence, considerando a tabela: 61 Brasilia ; 71 Salvador ; 11 Sao Paulo ; 21 Rio de Janeiro ; 32 Juiz de Fora ; 19 Campinas ; 27
### Vitoria ; 31 Belo Horizonte. Q:1050

n = int(input())

if n == 61:
	print("Brasilia")
elif n == 71:
	print("Salvador")
elif n == 11:
	print("Sao Paulo")
elif n == 21:
	print("Rio de Janeiro")
elif n == 32:
	print("Juiz de Fora")
elif n == 19:
	print("Campinas")
elif n == 27:
	print("Vitoria")
elif n == 31:
	print("Belo Horizonte")
else:
	print("DDD nao cadastrado")
