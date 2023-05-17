def apply_discounts(products, stocks):
    for i in stocks:
        n = int(stocks[i][:-1])/100
        stocks[i] = n
    for j in products:
        if j in stocks.keys():
            products[j]=round(products[j] - products[j]*stocks[j],2)
    return products


products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
stocks = {'Boiled sausage': '33%', 'Juice J7 (orange)': '12%', 'Trout (Seven Seas)': '18%'}

print(apply_discounts(products, stocks))


## {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 133.99, 'Juice J7 (orange)': 105.59, 'Trout (Seven Seas)': 327.99}
