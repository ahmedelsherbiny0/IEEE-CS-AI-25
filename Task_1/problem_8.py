text = input()
reverse = text[::-1]

flag = reverse == text 

print(f"The word '{text}' is{'' if flag else ' not'} a palindrome.")