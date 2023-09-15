from app.extensions import ma
from app.models.recipe import Recipe, Ingredient
from marshmallow import fields



# class RecipeSchema(ma.Schema):
#     class Meta:
#         model = Recipe
#         ordered = True
#
#     id = fields.Int()
#     Name = fields.Str(attribute="name")
#     calories_per_serving = fields.Int(attribute="calories")
#     prep_time = fields.Str()
#     servings = fields.Int()




class IngredientSchema(ma.Schema):
    class Meta:
        model = Ingredient
        ordered = True

    id = fields.Int()
    name = fields.Str()
    quantity = fields.Decimal()
    unit = fields.Str()


class RecipeSchema(ma.Schema):
    class Meta:
        model = Recipe
        ordered = True

    id = fields.Int()
    name = fields.Str()
    calories = fields.Int()
    prep_time = fields.Str()
    servings = fields.Int()
    ingredients = fields.List(fields.Nested(IngredientSchema))
    # id = ma.auto_field()
    # name = ma.auto_field()
    # prep_time = ma.auto_field()
    # servings = ma.auto_field()
    # calories = ma.auto_field()
    # ingredients = ma.auto_field()
