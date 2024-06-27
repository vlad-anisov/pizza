from odoo import models, fields, api
import json
from odoo.http import request


class CartLine(models.TransientModel):
    _name = "cart.line"

    product_id = fields.Reference(
        selection=lambda self: [(model_id.model, model_id.name) for model_id in self.env["ir.model"].sudo().search([])],
        string="Product",
    )
    product_name = fields.Char(string="Product name", compute="_compute_product_fields")
    product_description = fields.Char(string="Product description", compute="_compute_product_fields")
    product_image = fields.Image(string="Product image", compute="_compute_product_fields")
    product_price = fields.Float(string="Product price", digits=(16, 2), compute="_compute_product_fields")
    product_weight = fields.Integer(string="Product weight", compute="_compute_product_fields")

    total_price = fields.Float(string="Total Price", digits=(16, 2), compute="_compute_total_price")
    quantity = fields.Integer(string="Quantity")

    def _compute_product_fields(self):
        for record in self:
            product_id = record.product_id
            record.write({
                "product_name": product_id.name,
                "product_description": product_id.description,
                "product_image": product_id.image,
                "product_price": product_id.price,
                "product_weight": product_id.weight,
            })

    @api.depends("quantity")
    def _compute_total_price(self):
        for record_id in self:
            record_id.total_price = record_id.product_id.price * record_id.quantity

    def unlink(self):
        cart = json.loads(request.httprequest.cookies.get("cart", "[]"))
        for record in self:
            for item in cart:
                if item["product_id"] == record.product_id.id and item["product_model"] == record.product_id._name:
                    cart.remove(item)
        super().unlink()
        request.future_response.set_cookie("cart", json.dumps(cart))
        return self.env["cart"].open_cart()

    def reduce_quantity(self):
        cart = json.loads(request.httprequest.cookies.get("cart", "[]"))
        for record in self:
            for item in cart:
                if item["product_id"] == record.product_id.id and item["product_model"] == record.product_id._name and item["count"] > 0:
                    item["count"] -= 1
        request.future_response.set_cookie("cart", json.dumps(cart))
        return self.env["cart"].open_cart()

    def increase_quantity(self):
        cart = json.loads(request.httprequest.cookies.get("cart", "[]"))
        for record in self:
            for item in cart:
                if item["product_id"] == record.product_id.id and item["product_model"] == record.product_id._name:
                    item["count"] += 1
        request.future_response.set_cookie("cart", json.dumps(cart))
        return self.env["cart"].open_cart()
