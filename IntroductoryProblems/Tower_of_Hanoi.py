n = int(input())

def solve(n, src, des, hlpr):
    if n == 1:
        print(src, des)
        return 1

    move = solve(n-1, src, hlpr, des)
    move += 1 #current
    print(src, des)
    move += solve(n-1, hlpr, des, src)
    
    return move
    
print((2**n)-1 )
print(solve(n, 1, 3, 2))