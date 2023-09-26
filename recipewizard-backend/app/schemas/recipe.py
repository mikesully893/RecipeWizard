from app.extensions import ma
from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from marshmallow import fields, validate

allowed_units = ["qty", "tsp", "tbsp", "ml", "l", "g", "kg", "cup", "oz", "lb"]


class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        ordered = True

    unit = fields.Str(validate=validate.OneOf(allowed_units))


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        ordered = True

    ingredients = ma.Nested(IngredientSchema, many=True)
    steps = fields.Dict()
