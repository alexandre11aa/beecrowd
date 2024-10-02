# Não resolver desse modo, mas usando programação que usa um return dentro do outro

def dijkstra(N, station, e, 
             a_1, a_2, 
             t_1, t_2,
             x_1, x_2):

    ride, i = [[e], 1]

    if station == 1:
        ride.append(a_1[0])
    else:
        ride.append(a_2[0])

    while True:

        if station == 1:
            if a_1[i] <= a_2[i] + t_1[i-1]:
                ride.append(a_1[i])
            else:
                ride.append(a_2[i])
                ride.append(t_1[i-1])
                station += 1
        else:
            if a_2[i] <= a_1[i] + t_2[i-1]:
                ride.append(a_2[i])
            else:
                ride.append(a_1[i])
                ride.append(t_2[i-1])
                station -= 1
        
        i += 1

        if (i == N):
            break

    if station == 1:
        ride.append(x_1)
    else:
        ride.append(x_2)

    return ride

def p(r_1, r_2):
    print(r_1, sum(r_1))
    print(r_2, sum(r_2))

p(dijkstra(3, 1, 1, [1, 2, 3], [3, 2, 1], [1, 2], [2, 1], 1, 1),
  dijkstra(3, 2, 1, [1, 2, 3], [3, 2, 1], [1, 2], [2, 1], 1, 1)) # 7

p(dijkstra(10, 1, 3, [2, 6, 5, 0, 7, 9, 4, 4, 2, 2], [8, 0, 5, 8, 5, 2, 5, 9, 1, 7], [4, 6, 7, 2, 3, 6, 9, 1, 0], [1, 1, 8, 0, 0, 5, 0, 1, 7], 1, 0),
  dijkstra(10, 2, 2, [2, 6, 5, 0, 7, 9, 4, 4, 2, 2], [8, 0, 5, 8, 5, 2, 5, 9, 1, 7], [4, 6, 7, 2, 3, 6, 9, 1, 0], [1, 1, 8, 0, 0, 5, 0, 1, 7], 1, 0)) # 38

p(dijkstra(4, 1, 8, [8, 6, 5, 4], [8, 6, 3, 8], [7, 8, 0], [8, 0, 6], 8, 2),
  dijkstra(4, 2, 1, [8, 6, 5, 4], [8, 6, 3, 8], [7, 8, 0], [8, 0, 6], 8, 2)) # 28

p(dijkstra(6, 1, 6, [0, 5, 0, 8, 6, 3], [6, 9, 3, 0, 9, 8], [9, 9, 6, 5, 6], [2, 1, 3, 4, 6], 3, 5),
  dijkstra(6, 2, 1, [0, 5, 0, 8, 6, 3], [6, 9, 3, 0, 9, 8], [9, 9, 6, 5, 6], [2, 1, 3, 4, 6], 3, 5)) # 31

'''
TIME LIMIT EXCEEDED

while True:
    try:
        n = int(input())
        e1, e2 = [int(x) for x in input().split()]
        a1 = [int(x) for x in input().split()]
        a2 = [int(x) for x in input().split()]
        if n != 1:
            t1 = [int(x) for x in input().split()]
            t2 = [int(x) for x in input().split()]
        x1, x2 = [int(x) for x in input().split()]
        a1[0] += e1
        a2[0] += e2
        a1[len(a1) - 1] += x1
        a2[len(a2) - 1] += x2
        t = s = 0
        for c in range(2 ** n):
            p = f'{int(bin(s)[2:])}'.rjust(n, '0')
            tx = 0
            for d, e in enumerate(p):
                if e == '0':
                    tx += a1[d]
                elif e == '1':
                    tx += a2[d]
                if n != 1:
                    if d != 0:
                        if e != p[d - 1]:
                            if p[d - 1] == '0':
                                tx += t1[d - 1]
                            elif p[d - 1] == '1':
                                tx += t2[d - 1]
            if t == 0 or t > tx:
                t = tx
            s += 1
        print(t)
    except EOFError:
        break
'''
