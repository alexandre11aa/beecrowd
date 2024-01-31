### Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um diae
### terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. A entrada contém dois valores inteiros representan
### do a hora de início e a hora de fim do jogo. Apresente a duração do jogo conforme exemplo abaixo. Q:1046

ini, fim = input().split()

ini = int(ini)
fim = int(fim)

if ini >= fim:
	tempo = 24 - ini + fim
else:
	tempo = fim - ini

print("O JOGO DUROU %.i HORA(S)" % tempo)
