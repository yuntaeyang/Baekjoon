import math
n = int(input())
leng = len(str(n))
s = []
for i in str(n):
    if i != "0":
        s.append(int(i))
s = list(set(s))
for i in range(1,len(s)):
    s[0] = math.lcm(s[0],s[i])
k = s[0]
if n%k == 0:
    print(n)
else:
    cnt = 1
    check = 0
    while True:
        for i in range(0,10**cnt):
            if int(str(n) + "0"*(cnt-len(str(i))) + str(i)) % k == 0:
                print(int(str(n) + "0"*(cnt-len(str(i))) + str(i)))
                check = 1
                break
        if check == 1:
            break
        cnt += 1
        

