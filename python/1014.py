### Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (e
### m litros). O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e u
### m valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal. Apresente o valor que representa
### o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l". Q:1014

qui = int(input())
lit = float(input())

con = qui/lit

print("%.3f km/l" % con)
