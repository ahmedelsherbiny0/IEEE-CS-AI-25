import math

num = int(input())
sum = 0

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        sum += i
        sum += num / i

if sum == 2 * num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")