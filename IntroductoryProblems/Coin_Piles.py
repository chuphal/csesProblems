t = int(input())

for _ in range(t):
    p1, p2 = map(int, input().split())

    if p1 == 0 and p2 == 0:
        print("YES")

    elif (p1+p2)%3!=0 or p1 ==0 or p2 ==0 :
        print('NO')
    
    else:
        if (p1 > (2*p2)) or (p2 >(2*p1)):
            print("NO")
        
        else:
            print('YES')