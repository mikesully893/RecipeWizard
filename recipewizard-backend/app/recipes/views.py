from flask import jsonify, request

from app.extensions import db
from app.recipes import bp
from app.models.recipe import Recipe, Ingredient
from app.schemas.recipe import RecipeSchema, IngredientSchema

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        #recipes = Recipe.query.all()
        recipes = db.session.query(Recipe).all()
        return recipes_schema.dump(recipes)
    elif request.method == "POST":
        name = request.json["name"]
        prep_time = request.json["prep_time"]
        servings = request.json["servings"]
        calories = request.json["calories"]
        new_ingredients = []

        for i, ingredient in enumerate(request.json["ingredients"]):
            ingredient_name = ingredient["name"]
            ingredient_quantity = ingredient["quantity"]
            ingredient_unit = ingredient["unit"]

            new_ingredient = Ingredient(name=ingredient_name, quantity=ingredient_quantity, unit=ingredient_unit)
            new_ingredients.append(new_ingredient)
        new_recipe = Recipe(name=name, prep_time=prep_time, servings=servings, calories=calories)
        new_recipe.ingredients.extend(new_ingredients)
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.dump(new_recipe)


@bp.route("/ingredients/", methods=["GET"])
def get_ingredients():
    if request.method == "GET":
        #recipes = Recipe.query.all()
        ingredients = db.session.query(Ingredient).all()
        return ingredients_schema.dump(ingredients)
