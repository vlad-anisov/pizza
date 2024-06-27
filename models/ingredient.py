from odoo import models, fields


class Ingredient(models.Model):
    _name = "ingredient"

    name = fields.Char(string="Name")
