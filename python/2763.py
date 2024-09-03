#### O seu professor gostaria de fazer um programa com as seguintes características: Leia os dados de um CPF no formato XXX.YYY.ZZ
#### Z-DD; Imprima os quatro números, sendo um valor por linha. Entrada A entrada consiste vários arquivos de teste. Em cada arqui
#### vo de teste tem uma linha. A linha tem o seguinte formato XXX.YYY.ZZZ-DD, onde XXX, YYY, ZZZ, DD são números inteiros. Confor
#### me mostrado no exemplo de entrada a seguir. Saída Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de  saída
#### tem quatro linhas com um número inteiro em cada uma delas, conforme foi entrado. Conforme mostra o exemplo de saída a seguir.
#### Q:2763

cpf = input()

print(cpf[0]  + cpf[1] + cpf[2])
print(cpf[4]  + cpf[5] + cpf[6])
print(cpf[8]  + cpf[9] + cpf[10])
print(cpf[12] + cpf[13])
