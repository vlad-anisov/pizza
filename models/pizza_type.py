from odoo import models, fields


class PizzaType(models.Model):
    _name = "pizza.type"
    _inherit = "product"

    ingredient_ids = fields.Many2many("ingredient", string="Ингредиенты")

    def open_pizza_configurator(self):
        pizza_configurator_id = self.env["pizza.configurator"].create({
            "type_id": self.id,
        })
        return {
            "type": "ir.actions.act_window",
            "name": " ",
            "res_model": "pizza.configurator",
            "views": [[False, "form"]],
            "target": "new",
            "res_id": pizza_configurator_id.id,
        }
