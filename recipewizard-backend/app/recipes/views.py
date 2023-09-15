from flask import jsonify, request, make_response
from marshmallow import ValidationError
from sqlalchemy import exists

from app.extensions import db
from app.models.ingredient import Ingredient
from app.recipes import bp
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeSchema, IngredientSchema

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        recipes = db.session.query(Recipe).all()
        return recipes_schema.dump(recipes)
    elif request.method == "POST":
        try:
            recipe_schema.load(request.json)
        except ValidationError as err:
            response = make_response(err.messages, 400)
            return response

        name = request.json["name"]
        prep_time = request.json["prep_time"]
        servings = request.json["servings"]
        calories = request.json["calories"]
        steps = request.json["steps"]
        new_ingredients = []

        for ingredient in request.json["ingredients"]:
            ingredient_name = ingredient["name"]
            ingredient_quantity = ingredient["quantity"]
            ingredient_unit = ingredient["unit"]
            queried_ingredient = (
                db.session.query(Ingredient)
                .filter(
                    Ingredient.name == ingredient_name,
                    Ingredient.quantity == ingredient_quantity,
                    Ingredient.unit == ingredient_unit,
                )
                .first()
            )

            if queried_ingredient:
                new_ingredients.append(queried_ingredient)
            else:
                new_ingredient = Ingredient(
                    name=ingredient_name,
                    quantity=ingredient_quantity,
                    unit=ingredient_unit,
                )
                new_ingredients.append(new_ingredient)

        new_recipe = Recipe(
            name=name, prep_time=prep_time, servings=servings, calories=calories, steps=steps
        )
        new_recipe.ingredients.extend(new_ingredients)
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.dump(new_recipe)


@bp.route("/<int:recipe_id>/", methods=["GET"])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return recipe_schema.dump(recipe)


@bp.route("/<int:recipe_id>/", methods=["PUT"])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if request.method == "PUT":
        try:
            recipe_schema.load(request.json)
        except ValidationError as err:
            response = make_response(err.messages, 400)
            return response

        recipe.name = request.json["name"]
        recipe.prep_time = request.json["prep_time"]
        recipe.servings = request.json["servings"]
        recipe.calories = request.json["calories"]
        new_ingredients = []
        recipe.ingredients = []

        for ingredient in request.json["ingredients"]:
            ingredient_name = ingredient["name"]
            ingredient_quantity = ingredient["quantity"]
            ingredient_unit = ingredient["unit"]
            queried_ingredient = (
                db.session.query(Ingredient)
                .filter(
                    Ingredient.name == ingredient_name,
                    Ingredient.quantity == ingredient_quantity,
                    Ingredient.unit == ingredient_unit,
                )
                .first()
            )

            if queried_ingredient:
                new_ingredients.append(queried_ingredient)
            else:
                new_ingredient = Ingredient(
                    name=ingredient_name,
                    quantity=ingredient_quantity,
                    unit=ingredient_unit,
                )
                new_ingredients.append(new_ingredient)

        recipe.ingredients.extend(new_ingredients)
        db.session.add(recipe)
        db.session.commit()
        return recipe_schema.dump(recipe)


@bp.route("/<int:recipe_id>/", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    response = make_response([], 200)
    return response


@bp.route("/ingredients/", methods=["GET"])
def get_ingredients():
    if request.method == "GET":
        # recipes = Recipe.query.all()
        ingredients = db.session.query(Ingredient).all()
        return ingredients_schema.dump(ingredients)
