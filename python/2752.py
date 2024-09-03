#### O seu professor de programação gostaria que você fizesse um programa com as seguintes características: Crie uma variável para
#### armazenar 50 caracteres; Atribua a variável anterior a frase: "AMO FAZER EXERCICIO NO URI"; Mostre na primeira linha o caráct
#### er <, o valor armazenado na variável com o formato "%s" e o carácter >; Mostre na linha seguinte o carácter < , o valor armaz
#### enado na variável com o formato "%30s" e o carácter >; Mostre na linha seguinte o carácter < , o valor armazenado na variável
#### com o formato "%.20s" e o carácter >; Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%
#### -20s" e o carácter >; Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30s" e o caráct
#### er >; Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.30s" e o carácter >; Mostre  na
#### linha seguinte o carácter < , o valor armazenado na variável com o formato "%30.20s" e o carácter >; Mostre na linha seguinte
#### o carácter < , o valor armazenado na variável com o formato "%-30.20s" e o carácter >; Entrada / Não há. / Saída / O resultad
#### o de seu programa deve ser escrito conforme o exemplo da saída. Q:2752

variavel = 'AMO FAZER EXERCICIO NO URI'

print('<%s>'       % variavel)
print('<%30s>'     % variavel)
print('<%.20s>'    % variavel)
print('<%-20s>'    % variavel)
print('<%-30s>'    % variavel)
print('<%.30s>'    % variavel)
print('<%30.20s>'  % variavel)
print('<%-30.20s>' % variavel)
