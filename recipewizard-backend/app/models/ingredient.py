# from app.extensions import db
#
#
# class Ingredient(db.Model):
#     #__tablename__ = "ingredients"
#
#     id = db.Column(db.Integer, primary_key=True)
#     recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
#     quantity = db.Column(db.Double)
#     unit = db.Column(db.String(150))
#     name = db.Column(db.String(150))
#
#     def __repr__(self):
#         return f"<Ingredient {self.name}>"
