n = int(input())

summ  = (n+1)*n//2

if summ&1:
    print('NO')

else:
    print("YES")
    half = summ//2
    s1 = []
    s2 = []

    for i in range(n, 0, -1):
        if (half - i)>= 0:
            s1.append(i)
            half -= i 
        
        else:
            s2.append(i)

    print(len(s1))
    for i in range(len(s1) -1):
        print(s1[i], end= " ")
    
    print(s1[-1])

    print(len(s2))
    for i in range(len(s2)):
        print(s2[i], end=' ')
    
