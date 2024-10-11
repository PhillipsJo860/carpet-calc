# Joshua Phillips
# 10/11/24
# Carpet Calculator Project.

# Input
welcome = print('Welcome to Joshua\'s Carpet Calculator or JCC for short! In this project you can calculate the amount of carpet you will need to buy in order to fill out the floor with your carpet of choice and find the price of said carpet.')
length = float(input('Please enter the length of your room (in feet): ' ))
width = float(input('Please enter the width of your room (in feet): '))
price = float(input('Please enter the price per square yard(PPSY) of the carpet you want to use. This is only within the limits of $2.00 through $4.50, anything outside of this price range will invalidate the calculator. PPSY: $'))

# Process
area_feet = length * width
area_yards_flat = area_feet / 3
area_yards = round(area_yards_flat, 2)
subtotal_flat = area_yards * price
subtotal = round(subtotal_flat, 2)
tax_flat = subtotal * 0.06
tax = round(tax_flat, 2)
total_flat = subtotal + tax
total = round(total_flat, 2)


# Output
if price >= 2.00 and price <= 4.50:
    print(f'''  AMOUNT: You will need to buy a rounded area of {area_yards}yards to fool your room with your desired carpet.
      SUBTOTAL: ${subtotal}
      STATE TAX: ${tax}
      TOTAL: ${total}''')
else:
    print('The PPSY you entered does not follow the instructions given, please go back and read the instructions.')