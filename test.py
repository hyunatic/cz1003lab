G = 'G'
Y = 'Y'
B = 'B'
O = 'O'
logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, G, O,
    O, O, O, O, O, O, O, O,
    ]
print(logo)
print()
logo = map(lambda x: O if x == G else G, logo)
print(list(logo)) 