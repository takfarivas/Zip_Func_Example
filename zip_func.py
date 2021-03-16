# Items
items = ['Apples', 'Bananas', 'Oranges']
# Counts for how much items we buy
counts = [6, 7, 2]
# The prices for each item
prices = [0.55, 0.99, 0.45]

# Zipping the items, counts and prices
zipped = list(zip(items, counts, prices))

# Printing how much we have to get for buying each
for (item, count, price) in zipped:
    print(f'If you buy {count} {item} you will pay {count * price} $')

    
# No copyright stuff or smething free you can use it in every moment you want
