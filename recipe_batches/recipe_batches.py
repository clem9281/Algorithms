#!/usr/bin/python

import math
from timeit import timeit

# complexity of n * batches? so O(n)?
def recipe_batches(recipe, ingredients):
    batches = 0
    # keep looping, once we one out of an ingredient we'll return and that will stop everything
    while True:
        # as long as we haven't returned loop through the recipe
        for key in recipe:
            # if we don't even have that ingredient stop everything, we can't make this recipe
            if key not in ingredients:
                return 0
            # else subtract what we need from the recipe from the ingredients
            ingredients[key] = ingredients[key] - recipe[key]
            # if what's left in that ingredient it negative then the last batch was the last one we could make, return however many batches we've made
            if ingredients[key] < 0:
                return batches
        batches += 1


def recipe_batches_recursive(recipe, ingredients, batches=0):
    for key in recipe:
        # if we don't even have that ingredient stop everything, we can't make this recipe
        if key not in ingredients:
            return 0
        # else subtract what we need from the recipe from the ingredients
        ingredients[key] = ingredients[key] - recipe[key]
        # if what's left in that ingredient it negative then the last batch was the last one we could make, return however many batches we've made
        if ingredients[key] < 0:
            return batches
    # if we've reached the end of the loop, we know we had enough ingredients for this batch, run it again
    batches += 1
    return recipe_batches_recursive(recipe, ingredients, batches)


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )


# who's faster??

rec = {"milk": 100, "flour": 4, "sugar": 10, "butter": 5}
ing = {"milk": 1288, "flour": 9, "sugar": 95}
s = timeit("recipe_batches(rec, ing)", globals=globals(), number=1)
s_recur = timeit("recipe_batches_recursive(rec, ing)", globals=globals(), number=1)
print(f"Iterative: {s}")
print(f"Recursive: {s_recur}")

rec = {"milk": 100, "butter": 50, "cheese": 10}
ing = {"milk": 198, "butter": 52, "cheese": 10}
s = timeit("recipe_batches(rec, ing)", globals=globals(), number=1)
s_recur = timeit("recipe_batches_recursive(rec, ing)", globals=globals(), number=1)
print(f"Iterative: {s}")
print(f"Recursive: {s_recur}")

# Iterative: 6.700000000005313e-06
# Recursive: 3.900000000001125e-06
# Iterative: 6.599999999995498e-06
# Recursive: 2.1000000000048757e-06
# recursive much faster this time?
