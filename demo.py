
name = input("Enter name ")

age = input("How old are you? ")

voucher_no = input("What is your voucher no? ")

print(f"Your name is {name}, your age is {age} and you are using voucher no {voucher_no}")

print("Your name is {}, your age is {} and you are using voucher no: {}".format(name, age, voucher_no))

print("Your name is %s, your age is %s and you are using voucher no: %s" % (name, age, voucher_no))