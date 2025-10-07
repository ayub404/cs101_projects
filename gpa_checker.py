name = str(input('Students name: '))
gpa = float(input('Whats your GPA(0.0-4.0): '))
credit_hours = int(input('Whats your total credit hours: '))

deans_list = gpa>=3.5 and credit_hours>=12
is_gpa = bool(input('Is your gpa is less than 3.5?'))
needed_gpa = (gpa<3.5) * (3.5-gpa)
needed_credit_hours = (credit_hours < 12)* (12-credit_hours)
print(f"\n\nStudents name is {name}")
print(f"They made the dean list: {deans_list}")

print(f"How many GPA points need: {needed_gpa:.2f}")
print(f"How many credit hours need: {needed_credit_hours}")

