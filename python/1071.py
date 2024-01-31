### Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles. O arquivo de entrada contém d
### ois valores inteiros. O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os va
### lores fornecidos na entrada que deverá caber em um inteiro. Q:1071

x = int(input())
y = int(input())

if y < x:
	xx = y
	y = x
	x = xx

if x == y or (y - x == 1) or (y - x == -1):
    print(0)
    
elif (y - x == 3) or (y - x == -3):
    if x % 2 == 0:
        print(x + 1)
    elif y % 2 == 0:
        print(y - 1)
        
elif (y - x == 2) or (y - x == -2):
    if x % 2 == 0:
        print(x + 1)
    else:
        print(0)
        
else:
    con = x
    
    if con % 2 == 0:
        con = x + 1
    else:
        con = con + 2
    
    if x % 2 == 0:
	    x = x + 1
    else:
        x = x + 2

    nx = 0

    while con <= y:
        nx = nx + x
        x = x + 2
        con = con + 2
    print(nx)
