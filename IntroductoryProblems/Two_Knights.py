n = int(input())

for k in range(1, n+1):
    totalPlace = (k**2) * ((k**2) -1)//2
    notPlace = 4 * (k-1) *(k-2)
    
    totalWays = totalPlace - notPlace
    print(totalWays)
