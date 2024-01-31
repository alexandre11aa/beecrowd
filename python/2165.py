#### O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua t
#### arefa. A entrada é uma linha de texto T (1 ≤ |T| ≤ 500). A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas
#### ) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE". Q:2165

t = input()

if len(t) > 140:
	print("MUTE")
else:
	print("TWEET")
