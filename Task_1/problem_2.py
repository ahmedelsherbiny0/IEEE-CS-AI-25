inp = input("Enter the date: ")
date = inp.split()

day = int(date[1])
month = int(date[3])
year = int(date[5])

day += 7
if month == 2:
    if year % 4 == 0 and day > 29:
        day %= 29
        month += 1
    elif day > 28:
        day %= 28
        month += 1

elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    day %= 30
    month += 1
    
elif day > 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    day %= 31
    month +=1

if month > 12:
    month %= 12
    year += 1

print(f"Day:{day: 2} Month:{month: 2} Year: {year}")