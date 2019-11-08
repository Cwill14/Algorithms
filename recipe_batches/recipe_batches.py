#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  batches = 0
  results = []
  smallest = 0
  for v in ingredients:
  # for v in recipe:
  # for (k, v), (k2, v2) in zip(recipe, ingredients):  
  # for k, v in zip(recipe, ingredients):  
  # for k, v in enumerate(ingredients):
    # foo = ingredients.get(k, 0)
    # ingredients[k] = recipe.get(ingredients[k], ingredients[v])
    # ingredients[v2] = recipe.get(ingredients[v2], 0)
    # if ingredients[v2] not in recipe:
      # bar = recipe.get(ingredients[k], ingredients[k])
    # if ingredients[k2]
    # # elif ingredients[v] >= recipe[v]:
    # if ingredients[v2] >= recipe[v]:
    if ingredients[v] >= recipe[v]:
      # result = math.trunc(ingredients[v2] // recipe[v])
      result = math.trunc(ingredients[v] // recipe[v])
      results.append(result)
      smallest = results[0]
    else:
      smallest = 0
      # return smallest
  if len(results) == len(recipe):
    for i in results:
      print(f"smallest: {smallest}")
      if i < smallest:
        smallest = i
      print(f"smallest AFTER: {smallest}")
  else:
    smallest = 0
    
  batches = smallest
  return batches

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
test_recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
test_ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
test_ingredients1 = { 'milk': 123, 'butter': 150, 'flour': 25 }
test_ingredients2 = { 'milk': 310, 'butter': 120, 'flour': 25 }
test_ingredients3 = { 'milk': 341, 'butter': 150, 'flour': 25 }
test_recipe2 = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
test2_ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
# print(recipe_batches(test_recipe, test_ingredients))
# print(recipe_batches(test_recipe, test_ingredients1))
# print(recipe_batches(test_recipe, test_ingredients2))
# print(recipe_batches(test_recipe, test_ingredients3))
print(recipe_batches(test_recipe2, test2_ingredients))
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))