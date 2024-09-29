fruit_basket = {"apples": 5, "bananas": 4, "oranges": 8}

total_fruits = sum(fruit_basket.values())
print("The total number of fruits in the basket is:", total_fruits)
# It outputs: "The total number of fruits in the basket is: 17"

max_fruit = max(fruit_basket, key=fruit_basket.get)
print("The fruit with the most quantity is:", max_fruit)
# It outputs: "The fruit with the most quantity is: oranges"

min_fruit = min(fruit_basket, key=fruit_basket.get)
print("The fruit with the least quantity is:", min_fruit)
# It outputs: "The fruit with the least quantity is: bananas"
# key=fruit_basket.get tells min() to use the values of the dictionary for comparison.
# If we want to use the keys of the dictionary for comparison then:
min_key = min(fruit_basket)
print("The key with the smallest value is:", min_key)
# It outputs: "The key with the smallest value is: apples"

average_fruits = sum(fruit_basket.values()) / len(fruit_basket)
print("The average number of each type of fruit in the basket is:", average_fruits)
# It outputs: "The average number of each type of fruit in the basket is: 5.67"