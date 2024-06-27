from odoo import models, fields


class PizzaMainPage(models.Model):
    _name = "pizza.main.page"
    _description = "Pizza Main Page"

    carousel_image_ids = fields.Many2many('ir.attachment', string='Carousel Images')
    pizza_ids = fields.Many2many("pizza.pizza", string="Pizzas")
    pizza_type_ids = fields.Many2many("pizza.type", string="Pizzas")
    drink_ids = fields.Many2many("drink", string="Drink")

    def prev_slide(self):
        pass

    def next_slide(self):
        pass
