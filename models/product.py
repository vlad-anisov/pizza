from odoo import models, fields


class Product(models.AbstractModel):
    _name = "product"
    _inherit = "product.cart.mixin"

    name = fields.Char(string="Имя", required=True)
    description = fields.Char(string="Описание", required=True)
    image = fields.Image(string="Изображение", max_width=50, max_height=50, required=True)
    price = fields.Float(string="Цена", digits=(16, 2), required=True)
    weight = fields.Integer(string="Вес", required=True)
