#
# Complete the 'getProductSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY products
#  2. STRING search
#
#
########## Author: Leonardo Egito ############
########## Date: 07-25-2023 #####################
def getProductSuggestions(products, search):
    # Write your code here
    matches = []
    for item in search:
        searchMatch = []
        for product in products:
            if item == product[0:len(item)]:
                searchMatch.append(product)
        matches.append(searchMatch)
    return matches


searchItems = []
products = ['carpet', 'cart', 'car', 'camera', 'crate']
# searchItemsTest = ["c", "ca", "cam"]

searchItems.extend(input("Search terms: ").split())
print(f'Searched terms: {searchItems}')

result = getProductSuggestions(products, searchItems)
print(f'Result (search suggestions): {result}')