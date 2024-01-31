#### Raul Seixas cantava que nasceu há 10 mil anos atrás e não tinha nada nesse mundo que ele não sabia demais. Os Mamomas Assassin
#### as cantavam que mais de 10 mil anos "se passaram-se" [sic] quando eles repetiram a 5a série. Tantos eventos passados e o profe
#### ssor MC ficou curioso para saber em que ano tudo isso aconteceu. Você deve escrever um programa que, dada uma série de númerod
#### e anos transcorridos, mostre, para cada número, em que ano o evento aconteceu. Lembre-se de indicar se ele aconteceu A.C. (Ant
#### es de Cristo) ou D.C. (Depois de Cristo). A entrada tem várias linhas. A primeira tem um inteiro positivo N (1 ≤ N ≤ 100000).A
#### seguir existem N linhas. Cada uma dessas N linhas tem um único inteiro não negativo T, que indica o número de anos transcorrid
#### os até 2015 D.C. (0 ≤ T < 231). A saída tem N linhas. Em cada uma, deve ser indicado o ano A em que o correspondente tempo T a
#### conteceu. Veja o exemplo de saída. Q:1962

con = int(input())

for i in range(con):
	tempo = int(input())
	
	adc = 2015 - tempo

	if adc <= 0:
		print((tempo - 2014), "A.C.")
	else:
		print(adc, "D.C.")
