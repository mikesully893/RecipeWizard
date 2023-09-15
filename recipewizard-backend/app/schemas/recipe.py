from app.extensions import ma
from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from marshmallow import fields, validate


allowed_units = ["qty", "tsp", "tbsp", "ml", "l", "g", "kg", "cup", "oz", "lb"]


class IngredientSchema(ma.Schema):
    class Meta:
        model = Ingredient
        ordered = True

    name = fields.Str()
    quantity = fields.Decimal()
    unit = fields.Str(validate=validate.OneOf(allowed_units))


class RecipeSchema(ma.Schema):
    class Meta:
        model = Recipe
        ordered = True

    id = fields.Int(dump_only=True)
    name = fields.Str()
    calories = fields.Int(
        required=True,
        error_messages={
            "required": {"message": "Calories field is required", "code": 400}
        },
    )
    prep_time = fields.Str()
    servings = fields.Int()
    ingredients = fields.List(fields.Nested(IngredientSchema))
