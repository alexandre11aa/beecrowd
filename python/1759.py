#### Papai Noel está brincando com seus duendes para entretê-los durante a véspera do Natal. A brincadeira consiste nos elfos escr
#### e verem números em pedaços de papel e colocarem no gorro do Papai Noel. Após todos terminarem de colocar os números Noel sort
#### eia um papel e aquele número representa quantos "Ho" o Noel deve falar. Seu trabalho é ajudar o Papai Noel montando um proble
#### ma que mostre todos os "Ho" que ele deve falar dado o número sorteado. A entrada é composta por um único inteiro N (0 < N ≤ 1
#### 06) representando quantos "Ho" serão falados por Noel. A saída é composta por todos "Ho" que Papai Noel deve falar separadosp
#### or um espaço. Após o último "Ho" deve ser apresentado um "!" encerrando o programa. Q:1759

con = int(input())
ho = ""

for h in range(con - 1):
	ho += "Ho "

ho += "Ho!"
    
print(ho)
