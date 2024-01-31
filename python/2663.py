#### Em diversas competições acadêmicas, como a Olimpíada Brasileira de Informática (OBI), uma certa quantidade de competidores se
#### classifica de uma fase para a fase seguinte, garantindo uma das vagas disponíveis. Entretanto, normalmente essa quantidade év
#### ariável, pois dada uma certa quantidade mínima de classificados, é frequente que haja empate na última vaga de classificação.
#### Neste caso, é comum que todos os competidores empatados na última colocação se classifiquem. Sua tarefa é ajudar a calcular o
#### número de competidores classificados para a próxima fase. Você receberá uma lista de pontuações obtidas pelos competidores eo
#### número mínimo de vagas para a fase seguinte e você deve decidir quantos competidores de fato vão se classificar. A primeira l
#### inha da entrada contém um número inteiro N, 1 ≤ N ≤ 1000, representando o número de competidores. A segunda linha conterá umi
#### nteiro K, 1 ≤ K ≤ N, indicando o número mínimo de competidores que devem se classificar para a próxima fase. Em seguida, N li
#### nhas conterão, cada uma um número entre 1 e 1000, inclusive, correspondente á pontuação de um competidor. Seu programa deve i
#### mprimir uma linha, contendo o número de classificados para a próxima fase. Q:2663

N = int(input())
min_class = int(input())

c = []

for i in range(N):
    c.append(int(input()))

c.sort(reverse=True)

n_class = 0

for i in range(N):
    if c[i] < c[min_class-1]:
        break

    n_class += 1

print(n_class)
