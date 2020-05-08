pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

user_input = input()

if user_input in pasta:
    print("You can make pasta")
if user_input in apple_pie:
    print("You can make apple pie")
if user_input in ratatouille:
    print("You can make ratatouille")
if user_input in chocolate_cake:
    print("You can make chocolate cake")
if user_input in omelette:
    print("You can make omelette")