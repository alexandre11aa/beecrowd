### Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias Obs.: apenas para facilita
### r o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 1
### 2 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples. O
### arquivo de entrada contém um valor inteiro. Imprima a saída conforme exemplo fornecido. Q:1020

dias = int(input())

anos = dias / 365
meses = (dias % 365) / 30
diass = (dias % 365) % 30

print("%.i ano(s)" % anos)
print("%.i mes(es)" % meses)
print("%.i dia(s)" % diass)
