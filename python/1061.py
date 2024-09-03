### Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do
### mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termi
### na o evento. Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duraçã
### o deste evento. Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o eve
### nto vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceir
### a e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indican o o término do evento.
### Na saída, deve ser apresentada a duração do evento, no seguinte formato: W dia(s) ; X hora(s) ; Y minuto(s) ; Z segundo(s). Ob
### s: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto. Q:1061

aa, di = input().split()

di = int(di)

hri, mini, segi = map(int,input().split(":"))

bb, df = input().split()

df = int(df)

hrf, minf, segf = map(int,input().split(":"))

dias = df - di
horas = hrf - hri
minutos = minf - mini
segundos = segf - segi

if segundos < 0:
	segundos += 60
	minutos -= 1

if minutos < 0:
	minutos += 60
	horas -= 1

if horas < 0:
	horas += 24
	dias -= 1


print(dias,"dia(s)")
print(horas,"hora(s)")
print(minutos,"minuto(s)")
print(segundos,"segundo(s)")
