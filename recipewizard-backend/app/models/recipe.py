from app.extensions import db
from sqlalchemy_utils import JSONType


recipe_ingredients = db.Table(
    "recipe_ingredients",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), primary_key=True),
    db.Column(
        "ingredient_id", db.Integer, db.ForeignKey("ingredients.id"), primary_key=True
    ),
)


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    prep_time = db.Column(db.String(150))
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    ingredients = db.relationship(
        "Ingredient",
        secondary=recipe_ingredients,
        backref=db.backref("recipes", lazy="dynamic"),
        primaryjoin="Recipe.id == recipe_ingredients.c.recipe_id",
        secondaryjoin="Ingredient.id == recipe_ingredients.c.ingredient_id",
        lazy="dynamic",
    )
    steps = db.Column(JSONType)

    def __repr__(self):
        return f"<Recipe {self.name}>"
