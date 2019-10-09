#!/usr/bin/python

import math

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

