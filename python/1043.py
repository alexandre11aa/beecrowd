### Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triân
### gulo e apresente a mensagem: Perimetro = XX.X ; Em caso negativo, calcule a área do trapézio que tem A e B como base e C comoa
### ltura, mostrando a mensagem Area = XX.X ; A entrada contém três valores reais. O resultado deve ser apresentado com uma casa d
### ecimal. Q:1043

va, vb, vc = input().split()

va = float(va)
vb = float(vb)
vc = float(vc)

if ((va < (vb + vc)) and (va > (vb - vc)) and (va > (vc - vb)) and (vb < (va + vc)) and (vb > (va - vc)) and (vb > (vc - va)) and 
(vc < (va + vb)) and (vc > (va - vb)) and (vc > (vb - va))):
	per = va + vb + vc
	print("Perimetro = %.1f" % per)
else:
	area = ((va + vb) * vc)/2
	print("Area = %.1f" % area)
