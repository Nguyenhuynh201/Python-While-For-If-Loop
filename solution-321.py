price = int(input('Please enter the purchase price amount (in pennies): '))

change = 100 - price
print('Your change is: ')
#show change in quarter(s)
quarters = change // 25 
if quarters != 0:
    print(f'{quarters} quarters')
#show change in dime(s)
change %= 25
dimes = change // 10
if dimes != 0:
    print(f'{dimes} dimes')
#show change in nickle(s)
change %= 5
nickles = change // 5
if nickles != 0:
    print(f'{nickles} nickles')
#show change in pennies
pennies = change % 5
if pennies != 0:
    print(f'{pennies} pennies')

