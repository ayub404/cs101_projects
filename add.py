num1 = int(input("First number: "))
num2 = int(input("Second number:" ))
task = input("Which operation you wanna do:")
if task == '+':

    answer = num1+num2
    print(f"When you add these 2 numbers you get {answer}")
elif task == '-':
    answer = num1-num2
    print(f"When you subtract these 2 numbers you get {answer}")
elif task == '/':
    answer = num1/num2
    print(f"When you divide these 2 numbers you get {answer}")
elif task == '*':
    answer = num1*num2
    print(f"When you multiply these 2 numbers you get {answer}")
else:
    print("Choose another one!")