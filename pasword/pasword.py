password = input("Enter your password: ")

length = len(password)
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_symbol = any(not char.isalnum() for char in password)

score = 0

if length >= 8:
    score += 1
if has_digit:
    score += 1
if has_upper:
    score += 1
if has_symbol:
    score += 1

if score == 4:
    print("Strong password")
elif score >= 2:
    print("Medium password")
else:
    print("Weak password")
