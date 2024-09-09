"""kochbuch"""

import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipe1, new_servings1):
    factor = new_servings1 / recipe1['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe1['ingredients'].items()}
    return {
        'title': recipe1['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings1
    }


if __name__ == '__main__':
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4}'

    recipe = load_recipe(recipe_json)

    new_servings = 2

    adjusted_recipe = adjust_recipe(recipe, new_servings)

    print(json.dumps(adjusted_recipe, indent=4))
