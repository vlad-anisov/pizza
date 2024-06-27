from odoo import models, fields, api
from odoo.http import request
import json


class Cart(models.TransientModel):
    _name = "cart"

    line_ids = fields.Many2many("cart.line", string="Lines")
    total_price = fields.Float(string="Total Price", digits=(16, 2), compute="_compute_total_price")
    total_quantity = fields.Integer(string="Total Quantity", compute="_compute_total_quantity")

    @api.depends("total_quantity", "total_price")
    def _compute_display_name(self):
        for record in self:
            product_word = ""
            total_quantity = str(record.total_quantity)
            if total_quantity in ("11", "12", "13", "14"):
                product_word = "товаров"
            elif total_quantity[-1] == "1":
                product_word = "товар"
            elif total_quantity[-1] in ("2", "3", "4"):
                product_word = "товара"
            elif total_quantity[-1] in ("5", "6", "7", "8", "9", "0"):
                product_word = "товаров"
            record.display_name = f"{record.total_quantity} {product_word} на сумму {round(record.total_price, 2)} руб."

    @api.depends("line_ids.total_price")
    def _compute_total_price(self):
        for record_id in self:
            record_id.total_price = sum(record_id.mapped("line_ids.total_price"))

    @api.depends("line_ids.quantity")
    def _compute_total_quantity(self):
        for record_id in self:
            record_id.total_quantity = sum(record_id.mapped("line_ids.quantity"))

    @api.model
    def open_cart(self):
        cart = json.loads(request.httprequest.cookies.get("cart", "[]"))
        line_ids = self.env["cart.line"]
        for item in cart:
            line_ids += self.env["cart.line"].create({
                "product_id": self.env[item["product_model"]].browse(item["product_id"]),
                "quantity": item["count"],
            })
        cart_id = self.create({
            "line_ids": line_ids.ids
        })
        return {
            "type": "ir.actions.act_window",
            "name": " ",
            "res_model": "cart",
            "views": [[False, "form"]],
            "res_id": cart_id.id,
            "target": "new",
        }
