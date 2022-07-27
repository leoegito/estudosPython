from tokenize import Double

shoppingList = []
while True:
    product = input("Product: (type 'end' to exit) ")
    if product == "end" or product == "End" or product == "END":
        if len(shoppingList) > 0:
            if total > 0.0:
                print("Total: %.2f" % total)
        break
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    shoppingList.append([product, quantity, price])
    totalPrice = 0.0
    total = 0.0
    for item in shoppingList:
        print("%20s x %d x %5.2f = %6.2f" %
              (item[0], item[1], item[2], item[1]*item[2]))
        subTotalPrice = item[1] * item[2]
        total += subTotalPrice
    print("Total: %7.2f" % subTotalPrice)
