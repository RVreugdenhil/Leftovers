def recipe_finder(ingredients,recipes):
    """
    Parameters
    ----------
    ingredients : List with the chosen ingredients in the shape of [[id, ingredient]]
    recipes : List with the recipes

    Returns
    -------
    possible_recipes : List with recipes sorted on the scoring
    """
    possible_recipes = []
    for i in recipes:
        recipe_ingredients = []
        for j in range(len(i['ingredients'])):
            recipe_ingredients.append(i['ingredients'][j]['name'])
        common = [j for j in ingredients if j in recipe_ingredients]
        if common == ingredients:
            i['score'] = 0.3*i['review']-0.4*i['price']+0.3*i['complexity']
            possible_recipes.append(i)
        
    possible_recipes.sort(key=lambda x: x['score'], reverse=True)
    
    return possible_recipes