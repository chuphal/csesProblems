t = int(input())

for _ in range(t):
    y, x = map(int, input().split())
    
    if x >= y:
        ans = (x-1) * (x-1)
        add = 0

        if x&1:
            add = 2*x - y
        
        else:
            add = y 
        
        print(ans+add)
        
    else:
        ans = (y-1) * (y-1)
        add = 0

        if y&1:
            add = x

        else:
            add = 2*y -x
        
        print(ans+add)
        
