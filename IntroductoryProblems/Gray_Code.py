n = int(input())

def solve(n):
    if n == 1:
        return ['0', '1']
    
    prevGray = solve(n-1)
    reversePrevGray = prevGray[::-1]

    prevSize = len(prevGray)
    idx = 0
    while idx < prevSize:
        appendZero = "0" + prevGray[idx]
        prevGray[idx] = '1' + reversePrevGray[idx]

        prevGray.append(appendZero)
        idx += 1
    
    return prevGray

arr = solve(n)
for i in range(len(arr)):
    print(arr[i])