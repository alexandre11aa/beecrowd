#### Finalmente, o time da Universidade conseguiu a classificação para a Final Nacional da Maratona de Programação da SBC. Os três
#### membros do time e o técnico estão ansiosos para bem representar a Universidade, e além de treinar muito, preparam com todos o
#### s detalhes a sua viagem a São Paulo, onde será realizada a Final Nacional. Eles planejam levar na viagem todos os seus vários
#### equipamentos eletrônicos: celular, tablet, notebook, ponto de acesso wifi, câmeras, etc, e sabem que necessitarão de várias t
#### omadas de energia para conectar todos esses equipamentos. Eles foram informados de que ficarão os quatro no mesmo quarto de h
#### otel, mas já foram alertados de que em cada quarto há apenas uma tomada de energia disponível. Precavidos, os três membros do
#### time e o técnico compraram cada um uma régua de tomadas, permitindo assim ligar vários aparelhos na única tomada do quarto de
#### hotel; eles também podem ligar uma régua em outra para aumentar ainda mais o número de tomadas disponíveis. No entanto, comoa
#### s réguas têm muitas tomadas, eles pediram para você escrever um programa que, dado o número de tomadas em cada régua, determi
#### ne o número máximo de aparelhos que podem ser conectados à energia num mesmo instante. A entrada consiste de uma linha com qu
#### atro números inteiros T1, T2, T3, T4, indicando o número de tomadas de cada uma das quatro réguas (2 ≤ Ti ≤ 6). Seu programad
#### eve produzir uma única linha contendo um único número inteiro, indicando o número máximo de aparelhos que podem ser conectado
#### s à energia num mesmo instante. Q:1930

r1, r2, r3, r4 = map(int,input().split())

tomadas = r1 + r2 + r3 + r4 - 3

print(tomadas)
