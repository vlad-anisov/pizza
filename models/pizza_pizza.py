from odoo import models, fields, _

SIZE_TYPES = [
    ("small", "Маленькая"),
    ("medium", "Средняя"),
    ("large", "Большая"),
]

DOUGH_TYPES = [
    ("classic", "Классическое"),
    ("thin", "Тонкое"),
]


class Pizza(models.Model):
    _name = "pizza.pizza"
    _inherit = "product.cart.mixin"

    type_id = fields.Many2one("pizza.type", string="Тип", delegate=True, required=True, ondelete="cascade")
    ingredient_ids = fields.Many2many("ingredient", string="Ингредиенты", related="type_id.ingredient_ids", readonly=False)
    size = fields.Selection(SIZE_TYPES, string="Размер", default="medium", required=True)
    dough = fields.Selection(DOUGH_TYPES, string="Тесто", default="classic", required=True)
