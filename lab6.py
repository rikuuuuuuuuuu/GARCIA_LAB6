# Lab 6 - Registration Fee

age = int(input("Enter your age: "))
membership_status = input("Do you have a membership? (yes/no): ")
is_member = membership_status == "yes"

if age < 18:
    if is_member:
        fee = 450.00
    else:
        fee = 650.00
elif 18 <= age <= 65:
    if is_member:
        fee = 550.00
    else:
        fee = 750.00
else: 
    if is_member:
        fee = 400.00
    else:
        fee = 600.00

print(f"The registration fee is: {fee:.2f} pesos")
