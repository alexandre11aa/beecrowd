#### Péricles é um rapaz que tem um interesse único por história. Utilizando seu atualizadíssimo navegador de internet rapoza croma
#### da, conheceu até os sitios mais remotos e obscuros atrás de informações sobre a mitologia grega. Por ironia do destino, o nave
#### gador de Péricles acabou sendo infectado por um malware com uma caracterísica peculiar: cada vez que Péricles fechava uma aban
#### o seu navegador, outras duas abas apareciam! No entanto, quando Péricles clicou sem querer em uma das propagandas de uma aba,p
#### ercebeu que, por um erro do navegador, a aba foi encerrada (sem abrir outras abas). Por causa do malware, todas as abas possue
#### m irritantes propagandas. Sua tarefa é descobrir com quantas abas que o navegador de Péricles ficou, sabendo o número iniciald
#### e abas e a sequência de ações de Péricles. As ações podem ser fechou (quando Péricles fechou uma aba) ou clicou (quando Péricl
#### es clicou em uma propaganda). A entrada é iniciada por uma linha contendo dois números inteiros positivos, N e M (0 < N, M < 5
#### 00), representando o número inicial de abas e o número de ações de Péricles. Cada linha subsequente contém uma ação (fechou ou
#### clicou). Naturalmente, o número de abas é sempre maior ou igual a zero. A saída deve ser uma linha contendo o número final dea
#### bas. Q:2061

a, t = map(int,input().split())

s = a

for i in range(t):
	fc = input()
	
	if fc == "fechou":
		s += 1
	else:
		s -= 1

print(s)
