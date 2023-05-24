import random

password_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#£$€%^&*()-+{}:?~[]<>/\;,-_=`|"
length_password = int(input("Enter the length of the password: "))
a = "".join(random.sample(password_chars,length_password))

if length_password >= 8:
    print(f"Your password is: {a}")
else:
    print("Password Length is too short please retry")