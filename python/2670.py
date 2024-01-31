#### O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da
#### SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expres
#### so. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam m
#### uito tempo subindo e descendo escadas. Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde tra
#### balha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou desce
#### r um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total ga
#### sto subindo e descendo escadas. Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gas
#### to pelos funcionários subindo e descendo escadas. A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1 , A2 , A3 ≤ 1000), um
#### por linha, onde Ai representa o número de pessoas que trabalham no i-ésimo andar. Seu programa deve imprimir uma única linha,
#### contendo o número total de minutos a serem gastos com o melhor posicionamento possível da máquina. Q:2670

A = []

for i in range(3):
    A.append(int(input()))

tempos = [A[1] * 2 + A[2] * 4,
          A[0] * 4 + A[1] * 2,
          A[0] * 2 + A[2] * 2]

tempos.sort()

print(tempos[0])
