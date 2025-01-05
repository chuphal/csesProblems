string = input()

ans = 1
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1 
    else:
        count = 1
    ans = max(count, ans)

print(ans)