import random
import string
letters='abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnoprstuvwxyz'
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='1234567890'
symbols='!@#$%^&*()_+-={}[]"":;?/>.<,~`'
length=int(input("Enter the number of character you need in your password: "))
print(" To get a Generated Password,select the one below ")
print("1.Generate a passowrd with mixed Numbers ,symbols,Uppercase,Lowercase")
print("2.Generate the password with specific characters Type")
print("3.EXIT")
choice= input("Enter whats your choice!")
if choice=="1":
    all_char=lowercase+uppercase+numbers+symbols+letters
    Password=" "
    for i in range(length):
        Password+=random.choice(all_char)
        print("Your GENERATED PASSWORD is:",Password)
elif choice=="2":
    include_letters=input("Need letters to be included(yes/no) :").lower()
    include_numbers=input("Need numbers to be included(yes/no) :").lower()
    include_symbols=input("Need symbols to be included? (yes/no) :").lower()
    char=" "
    if include_letters=="yes":
        char+=string.ascii_letters
    if include_numbers=="yes":
        char+=string.digits
    if include_symbols=="yes":
        char==string.punctuation
    if char==" ":
        print("None selected,cannot Generate your password")
    else:
        Password=" "
        for i in range(length):
            Password+=random.choice(char)
            print("Your GENERATED PASSWORD is: ",Password)
elif choice=="3":
    print("EXIT")
else:
    print("INVALID CHOICE")