fruits = ["apple", "banana", "orange", "cherry", "tomato"]

def pluralize(word):
    if word[-1] == 'y':
        inflected_word = word[0:-1]+"ies"
    elif word[-1] == 's' or word[-1] == 'o':
        inflected_word = word + "es"
    else:
        inflected_word = word + "s"
    return inflected_word


quantities = {}
for fruit in fruits:
    inflected_fruit = pluralize(fruit)
    qty = int(raw_input("How many %s? " % inflected_fruit))
    quantities[fruit] = qty

for fruity in fruits:
    qty = quantities[fruity]
    if qty == 1:
        inflected_fruit = fruity
    else:
        inflected_fruit = pluralize(fruity)
    print "You should buy %d %s" % (quantities[fruity], inflected_fruit)