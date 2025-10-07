customer_name = str(input('Whats your name:'))

is_member = bool(input('Are you member(True/False); '))
is_loyalty = bool(input('Is your previous purchase was over 1000000 or equal(True/False): '))


purchases = ['Airpods', 'Phone', 'Charger']

quantity_airpods = int(input('How many Airpods you are gonna buy: '))
quantity_phone = int(input("How many Phones you are gonna buy: "))
quantity_charger = int(input('How many chargers you are gonna buy: '))

total_item = bool(input('Is your total items over 5 or equal(True/False): '))
is_shipping = bool(input('Is your total sales less than 500000(True/False): '))

airpods = float(100000)
phone = float(300000)
charger= float(50000)

subtotal = quantity_airpods * airpods+ quantity_charger * charger + quantity_phone* phone
subtotal_before = quantity_airpods * airpods+ quantity_charger * charger + quantity_phone* phone
# total_item = quantity_airpods + quantity_phone + quantity_charger

member_discount = 0.1
bulk_discount = 0.05
loyalty_discount = 0.03

tax_rate = 0.12

shipping = 25000
shipping = is_shipping * shipping
discounted_price_member = is_member * member_discount *subtotal
discounted_price_loyalty = is_loyalty * loyalty_discount * subtotal
discounted_price_bulk = total_item * bulk_discount * subtotal

discounts = discounted_price_bulk + discounted_price_loyalty + discounted_price_member

tax = subtotal * tax_rate
total_before_everything = subtotal_before +shipping
subtotal = subtotal - discounts + shipping



print(f'\nCustomer name: {customer_name}\n')
print(f'Membership status: {is_member}\n')
print(f'Purchased Items: {purchases}\n')
print(f'Subtotal before all the discounts and without tax: {subtotal_before}\n')

print(f'Member discount: {is_member}, discounted_price: {discounted_price_member}\n')
print(f'Bulk discount: {total_item}, discounted_price: {discounted_price_bulk}\n')
print(f'Loyalty discount: {is_loyalty}, discounted_price: {discounted_price_loyalty}\n')

print(f'Total discounts: {discounts}\n')
print(f'Subtotal after all discounts: {subtotal_before - discounts}\n')
print(f'Tax amount: {tax:.2f}')
print(f'Shipping cost with free shipping status: shipping cost: {shipping}\n')

print(f'Final price after all discounts and tax: {subtotal_before - discounts + shipping + tax}\n')

print(f'Total saved amount is: {total_before_everything - subtotal}\n')