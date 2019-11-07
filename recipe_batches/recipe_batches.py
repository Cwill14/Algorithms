#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  pass 

# check ingredients to see if they are >= same key in recipe. 

#   initialize batches = 0
#   for each key, value in zip ingredients, recipe
#   zip here
#   if key's value >= same key's value in recipe
#   set a bool to true ?
#   while true?
#   if true for all keys, amount of batches += 1
#     then subtract values in ingredients by values in recipe_batches
#     then run check again somehow, maybe have to use recursion? :( might not have to because we are in a loop
#   else set bool to false, return batches
# return  batches

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))