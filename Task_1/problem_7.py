import math

num = int(input())
primes = []

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            primes.append(i)
        
        k = num / i
        flag = True
        for j in range(2, int(math.sqrt(k)) + 1):
            if k % j == 0:
                flag = False
                break
        if flag:
            primes.append(int(k))
            
if num == 2:
    primes.append(num)

if len(primes) == 0:
    primes.append(num)

if num == 1:
    print(f"This number has no Prime Factors!")

else:
    print(f"Prime Factors: ", end="")
    print(*primes,sep=", ")