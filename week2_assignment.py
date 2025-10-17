customer_name = str(input('Whats your name: '))

is_member = bool(input('Are you member(True/False); '))
is_loyalty = bool(input('Is your previous purchase was over 1000000 or equal(True/False): '))


print('Which items you want to buy:(Please pick at least 3 products)')
item_1 = input(str('WHat is the first item: '))
price_1 = float(input('Whats is the price of the first item: '))
item_2 = input(str('WHat is the second item: '))
price_2 = float(input('Whats is the price of the second item: '))
item_3 = input(str('WHat is the third item: '))
price_3 = float(input('Whats is the price of the third item: '))

quantity_item_1 = int(input(f'How many {item_1} you are gonna buy: '))
quantity_item_2 = int(input(f'How many {item_2} you are gonna buy: '))
quantity_item_3 = int(input(f'How many {item_3} you are gonna buy: '))

total_item = bool(input('Is your total items over 5 or equal(True/False): '))



subtotal = quantity_item_1 * price_1+ quantity_item_2 * price_2 + quantity_item_3* price_3
subtotal_before = quantity_item_1 * price_1+ quantity_item_2 * price_2 + quantity_item_3* price_3
# total_item = quantity_airpods + quantity_phone + quantity_charger

member_discount = 0.1
bulk_discount = 0.05
loyalty_discount = 0.03

tax_rate = 0.12

is_shipping = subtotal_before < 500000
shipping = 25000 if is_shipping else 0
discounted_price_member = is_member * member_discount * subtotal
discounted_price_loyalty = is_loyalty * loyalty_discount * subtotal
discounted_price_bulk = total_item * bulk_discount * subtotal

discounts = discounted_price_bulk + discounted_price_loyalty + discounted_price_member

tax = subtotal * tax_rate
total_before_everything = subtotal_before + shipping
subtotal = subtotal - discounts + shipping


print('*'*60)
print(f'\n                  Electronics store               ')
print('\n')
print('*'*60)
print(f'\nCustomer name: {customer_name}\n')
print(f'Membership status: {is_member}\n')
print(f'Purchased Items: {item_1, item_2, item_3}\n')
print(f'Subtotal before all the discounts and without tax: {subtotal_before}\n')
print('-'*60)
print(f'Member discount: {is_member}, discounted_price: {discounted_price_member:.2f}\n')
print(f'Bulk discount: {total_item}, discounted_price: {discounted_price_bulk:.2f}\n')
print(f'Loyalty discount: {is_loyalty}, discounted_price: {discounted_price_loyalty:.2f}\n')
print('-'*60)
print(f'Total discounts: {discounts:.2f}\n')
print(f'Subtotal after all discounts: {subtotal_before - discounts}\n')
print(f'Tax amount: {tax:.2f}')
print(f'Shipping cost with free shipping status: shipping cost: {shipping:.2f}\n')
print('-'*60)
print(f'Final price after all discounts and tax: {subtotal_before - discounts + shipping + tax}\n')

print(f'Total saved amount is: {total_before_everything - subtotal}\n')
print(f'          *** Thank you for your purchase *** \n')
print('*'*60)
