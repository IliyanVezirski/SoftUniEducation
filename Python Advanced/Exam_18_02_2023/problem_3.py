def shop_from_grocery_list(budget: int, *args):
    products_to_buy = args[0]
    for product in args[1:]:
        if product[0] in products_to_buy:
            if float(product[1]) <= budget:
                budget -= float(product[1])
                products_to_buy.remove(product[0])
            else:
                break
            if not products_to_buy:
                break
    if not products_to_buy:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f"You did not buy all the products. Missing products: {', '.join(products_to_buy)}."
