from sqlalchemy import String
from typing import List
from typing import Optional
from app.extensions import db
#from app.models.ingredient import Ingredient

#
# recipe_ingredients = db.Table(
#     "recipe_ingredients",
#     db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id"), primary_key=True),
#     db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredients.id"), primary_key=True)
# )


# class Base(db.DeclarativeBase):
#     pass


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    prep_time = db.Column(db.String(150))
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    ingredients = db.relationship("Ingredient", back_populates="recipe")
    # ingredients = db.relationship("Ingredient", secondary=recipe_ingredients, backref=db.backref("recipes", lazy="dynamic"),
    #                               primaryjoin="Recipe.id == recipe_ingredients.c.recipe_id",
    #                               secondaryjoin="Ingredient.id == recipe_ingredients.c.ingredient_id",
    #                               lazy="dynamic")

# class Recipe(Base):
#     __tablename__ = "recipes"
#
#     id: db.Mapped[int] = db.mapped_column(primary_key=True)
#     name: db.Mapped[str] = db.mapped_column(db.String(30))
#     prep_time: db.Mapped[str] = db.mapped_column(db.String(30))
#     servings: db.Mapped[int] = db.mapped_column(db.Integer)
#     calories: db.Mapped[int] = db.mapped_column(db.Integer)
#
#     def __repr__(self):
#         return f"<Recipe {self.name}>"


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    recipe = db.relationship("Recipe", back_populates="ingredients")
    quantity = db.Column(db.Double)
    unit = db.Column(db.String(150))
    name = db.Column(db.String(150))

    def __repr__(self):
        return f"<Ingredient {self.name}>"
