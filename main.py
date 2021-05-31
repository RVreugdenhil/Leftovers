from flask import Flask, render_template, request, json
from recipe_functions.recipe_finder import recipe_finder

app = Flask(__name__)

def suggestionFormat(json_link):
    res = []
    f = open(json_link)
    ingredients = json.load(f)
    for ingredient in ingredients:
        res.append(ingredient[1])
    return res

def readJson(json_link):
    f = open(json_link)
    res = json.load(f)
    f.close()
    return res

allIngredients = readJson("C:/Users/robbi/OneDrive/Documenten/Start_Up/Leftovers/Ariesshit/ingredients.json")
allRecipes = readJson("C:/Users/robbi/OneDrive/Documenten/Start_Up/Leftovers/Ariesshit/recipes.json")


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        selectedIngredients = request.form.getlist('ingredients[]')
        sortedRecipes = recipe_finder(selectedIngredients, allRecipes)
        return render_template("recipeshower.html", recipes = sortedRecipes)
    else:
        return render_template("index.html", allIngredients = allIngredients)



if __name__ == '__main__':
    app.run(debug=True)