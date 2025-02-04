sum = 0

while True:
    x = int(input(""))
    if not x == -1:
        sum += x
    else:
        break

print(f"Sum: {sum}")