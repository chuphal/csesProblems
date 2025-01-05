string = input()

ans =[]
def solve(arr, perms):
    if not arr:
        ans.append("".join(perms))
    
    for i in range(len(arr)):
        solve(arr[:i] + arr[i+1:], perms + [arr[i]])

arr = list(string)
# solve(arr, [])
# kat = sorted(set(ans))


def backtrack(arr, idx):
    if idx == len(arr):
        ans.append(''.join(arr))
        return 
    
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
    
        backtrack(arr.copy(), idx+1)
        # backtrack
        arr[idx] , arr[i] = arr[i], arr[idx]
    
    return 

backtrack(arr, 0)
kat = sorted(set(ans))

print(len(kat))
for i in range(len(kat)):
    print(kat[i])
    
    
    