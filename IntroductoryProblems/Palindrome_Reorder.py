string = input()

count = [0]*26

for i in range(len(string)):
    char = string[i]
    idx = ord(char) - ord("A")
    count[idx] += 1

odd = 0
even = 0
for i in range(26):
    if count[i]&1:
        odd +=1
    else:
        even += 1

if odd > 1:
    print('NO SOLUTION')

else:
    first = ''
    mid  = ''
    last = ''

    for i in range(26):
        if count[i] > 0:
            char = chr(i + ord('A'))
            if count[i]&1:
                mid += count[i] * char

            else:
                num = count[i]//2
                first += num * char 
                last = num * char + last 
        
    
    print(first + mid + last)