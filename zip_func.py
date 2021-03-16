items = ['Apples', 'Bananas', 'Oranges']
counts = [4, 6, 2]
prices = [0.59, 0.45, 0.99]

zipped = list(zip(items, counts, prices))

for (item, count, price) in zipped:
    print(f'If you buy {count} {item} you will pay {count * price} $')

