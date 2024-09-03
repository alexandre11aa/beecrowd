#### Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, d
#### evorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em2
#### 011. O restaurante Nathan’s Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. Eles produzem del
#### iciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não são tão bons. Eles desejam ser lis
#### tados no Livro de Recordes do Guinness, mas para isso devem preencher um formulário descrevendo os fatos básicos da competição
#### . Em particular, eles devem informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.V
#### ocê pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos cachorros-quentes. Dados o número total de cachorros-que
#### ntes consumidos e o número total de participantes na competição, você deve escrever um programa para determinar o número médio
#### de cachorros-quentes consumidos pelos participantes. A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤
#### H, P ≤ 1000) indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na com
#### petição. Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes c
#### onsumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto d
#### ecimal, arredondado se necessário. Q:2234

p, c = map(float,input().split())

print("%.2f" % (p/c))
