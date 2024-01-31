#### O Brasil é o país sede da copa esse ano. Porém, há muitas pessoas protestando contra o governo. Em redes sociais é possível v
#### er pessoas afirmando que não vai ter copa devido aos protestos. Mas esses rumores de que não haverá copa são totalmente falso
#### s, a presidente Dilma Roussef já avisou: vai ter copa sim, e se reclamar vai ter duas! A entrada contém vários casos de teste
#### e termina com EOF. Cada caso de teste consiste de uma linha contendo o número N de reclamações sobre a copa encaminhadas para
#### a presidente (0 ≤ N ≤ 100). Para cada teste, a saída consiste de uma linha dizendo "vai ter copa!" caso não haja reclamaçõesp
#### ara a presidente. Caso haja reclamações, a saída deverá dizer "vai ter duas!". Q:1564

while True:
	try:
		re = int(input())
		if re == 0:
			print("vai ter copa!")
		else:
			print("vai ter duas!")
	
	except EOFError:
		break
