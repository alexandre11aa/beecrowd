### Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo. Obs: O jogo tem
### duração mínima de um (1) minuto e duração máxima de 24 horas. Quatro números inteiros representando a hora de início e fim doj
### ogo. Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)”. Q:1047

hi, mi, hf, mf = map(int,input().split())

ti = (hi * 60) + mi
tf = (hf * 60) + mf

if ti > tf:
	xx = tf
	tf = ti
	ti = xx
    
if hf < hi and mf < mi:
	th = ((24 - hi) + hf) - 1
	tm = (60 - mi) + mf
	print("O JOGO DUROU %.i HORA(S) E %.i MINUTO(S)" % (th,tm))
    
elif hi == hf and mi > mf:
	tt = mi - mf
	tm = 60 - tt
	print("O JOGO DUROU 23 HORA(S) E %.i MINUTO(S)" % (tm))
    
elif hi == hf and mi < mf:
	tm = mf - mi
	print("O JOGO DUROU 0 HORA(S) E %.i MINUTO(S)" % (tm))
    
elif hi == hf and mi == mf:
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    
else:
	if hi < hf:
		tt = tf - ti
		th = int(tt / 60)
		tm = int(tt - (th * 60))
		print("O JOGO DUROU %.i HORA(S) E %.i MINUTO(S)" % (th,tm))
    
	elif hi > hf:
		tt = 720 + ((hf + 12 - hi) * 60)
		th = int(tt / 60)
		tm = int(tt - (th * 60))
		print("O JOGO DUROU %.i HORA(S) E %.i MINUTO(S)" % (th,tm))
