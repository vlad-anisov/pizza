from odoo import models
from odoo.exceptions import UserError


class PizzaConfigurator(models.TransientModel):
    _name = "pizza.configurator"
    _inherit = "pizza.pizza"

    def get_or_create_pizza(self):
        self.ensure_one()
        if not self.size or not self.dough:
            raise UserError("Size or dough of pizza is not specified")
        pizza_id = self.env["pizza.pizza"].search(
            [("type_id", "=", self.type_id.id), ("ingredient_ids", "=", self.ingredient_ids.ids),
             ("size", "=", self.size), ("dough", "=", self.dough)],
            limit=1
        )
        if not pizza_id:
            pizza_id = self.env["pizza.pizza"].create({
                "type_id": self.type_id.id,
                "ingredient_ids": self.ingredient_ids.ids,
                "size": self.size,
                "dough": self.dough,
            })
        return pizza_id

    def add_pizza_to_cart(self):
        pizza_id = self.get_or_create_pizza()
        return pizza_id.add_to_cart()
