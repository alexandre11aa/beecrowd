#### O seu professor gostaria de fazer um programa com as seguintes características: Leia uma data no formato DD/MM/AA; Imprima  a
#### data no formato MM/DD/AA; Imprima a data no formato AA/MM/DD; Imprima a data no formato DD-MM-AA. Entrada A entrada  consiste
#### vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem o seguinte formato DD/MM/AA onde DD, MM, AA são
#### números inteiros. Conforme mostrado no exemplo de entrada a seguir. Saída Para cada arquivo da entrada, terá um arquivo de sa
#### ída. O arquivo de saída tem três linhas conforme os procedimentos 2, 3 e 4. Conforme mostra o exemplo de saída a seguir. Q:27
#### 64

n_1, n_2, n_3 = input().split("/")

print(n_2 + "/" + n_1 + "/" + n_3)
print(n_3 + "/" + n_2 + "/" + n_1)
print(n_1 + "-" + n_2 + "-" + n_3)
