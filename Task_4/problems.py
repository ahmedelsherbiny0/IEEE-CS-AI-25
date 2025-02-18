import math

def get_numbers():
    global numbers
    while True:
        try:
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            break
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")
    
    global length
    length = len(numbers)
    
def sort_numbers(list):
    length = len(list)
    for i in range(length):
        for j in range(length - i - 1):
            if list[j] > list[j + 1]:
                [list[j], list[j + 1]] = [list[j + 1], list[j]] 
    return list
    
def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def find_mean(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / length
       
def find_mod(numbers):
    freq = {}
    for number in numbers:
        if not number in freq:
            freq[number] = 1
        else:
            freq[number] += 1
    return [key for key, val in freq.items() if val == max(freq.values())]

def find_median(numbers):
    sortedNumbers = sort_numbers(numbers)
    n = len(sortedNumbers)
    if n % 2 == 1:
        return sortedNumbers[n // 2]
    else:
        return (sortedNumbers[n // 2] + sortedNumbers[n // 2 - 1]) / 2
        
def find_range(numbers):
    sortedNumbers = sort_numbers(numbers)
    return sortedNumbers[length - 1] - sortedNumbers[0]

def find_variance(numbers):
    mean = find_mean(numbers)
    sum = 0
    for number in numbers:
        sum += (number - mean) ** 2
    return sum / (length - 1)

def find_STD(numbers):
    variance = find_variance(numbers)
    return math.sqrt(variance)

def find_Quartiles(numbers):
    Q2 = find_median(numbers)
    sortedNumbers = sort_numbers(numbers)
    
    if length % 2 == 1:
        lower_half = sortedNumbers[:length // 2]
        upper_half = sortedNumbers[length // 2 + 1:]
    else:
        lower_half = sortedNumbers[:length // 2]
        upper_half = sortedNumbers[length // 2:]

    Q1 = find_median(lower_half)
    Q3 = find_median(upper_half)
    return (Q1, Q2, Q3)

def find_IQR(numbers):
    quartiles = find_Quartiles(numbers)
    return quartiles[2] - quartiles[0]
    
while True:
    get_numbers()
    # print(numbers)
    # print(sort_numbers(numbers))
    print(f"Min: {find_min(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Mean: {find_mean(numbers): .2f}")
    print(f"Mod: {find_mod(numbers)}")
    print(f"Median: {find_median(numbers)}")
    print(f"Range: {find_range(numbers)}")
    print(f"Variance: {find_variance(numbers): .2f}")
    print(f"Standard Deviation: {find_STD(numbers): .2f}")
    print(f"Quartiles: {find_Quartiles(numbers)}")
    print(f"Interquartile Range (IQR): {find_IQR(numbers)}")
    
    out = input("Press Q to quit or any key to continue: ")
    if out.upper() == 'Q':
        break