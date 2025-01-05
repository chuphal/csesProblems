n = int(input())

if  1 < n < 4:
    print("NO SOLUTION")

else: 
    for i in range(n-1, 0, -2):
        print(i, end= " ")
    
    for j in range(n, 0, -2):
        print(j, end= " ")
