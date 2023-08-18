import pandas as pd 
import numpy as np 

number = 2
string = 'health'
mylist = [1, 3, 5, 7, 9]
mydictionary = {
'name': 'stephen',
'ID': 123445656,
'favorite fruits': ['watermelon', 'banana', 'peach'],
'address': {
    'street': 'nicolls road',
    'county': 'suffolk',
    'city': 'long island'
}
}

def discount_calculation(price, age):
    if age <= 12:
        discount = 0.25
    else:
        discount = 0.05
    discounted_price = price + (price * discount)
    return discounted_price

original_price = 15
customer_age = 11
final_price = discount_calculation(original_price, customer_age)
print('Original Price:', original_price)
print('Customer Age:', customer_age)
print('Final Price:', final_price)