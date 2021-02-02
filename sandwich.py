import pyinputplus as pyip 

bread = pyip.inputMenu(choices=['white', 'wheat', 'sourdough'], lettered=True)

protein = pyip.inputMenu(choices=['chicken', 'turkey', 'ham', 'tofu'], lettered=True)

cheese = pyip.inputYesNo(prompt='Do you want cheese? ')
if cheese == 'yes':
    typeOfCheese = pyip.inputMenu(choices=['cheddar', 'swiss', 'mozzarella'])

toppings = pyip.inputYesNo(prompt='Would you like extra toppings added in your sandwich? ')

numOfSandwiches = pyip.inputInt(prompt='How many sandwiches would you like? ', min=1)

breads = {
    'white': 1,
    'wheat': 1.25,
    'sourdough': 1.5
}

proteins = {
    'chicken': 1,
    'turkey': 1.5,
    'ham': 2,
    'tofu': 3
}

cheeses = {
    'cheddar': 0.5,
    'swiss': 0.5,
    'mozzarella': 0.25
}

price = breads[bread] + proteins[protein] + cheeses[typeOfCheese]

if numOfSandwiches is 1:
    print(f'The customer wants {numOfSandwiches} sandwich')
    print(f'The total price of the sandwich is ${price:.2f}')
else:
    print(f'The customer wants {numOfSandwiches} sandwiches')
    print(f'The total price of the sandwich is ${price * numOfSandwiches:.2f}')