import string
password=input("Enter your password\n")

has_upper=any(c.isupper() for c in password)
has_lower=any(c.islower() for c in password)
has_digit=any(c.isdigit() for c in password)
has_special=any(c in string.punctuation for c in password)

if len(password)<8:
    print("Weak: Add atleast Eight character")
elif not has_upper:
    print("Weak: Add atleast one upper case")
elif not has_lower:
    print("Weak: Add atleast one lower case")
elif not has_digit:
    print("Weak: Add atleast one digit case")
elif not has_special:
    print("Weak: Add atleast one special case")
else:
    print("Your password is Strong")