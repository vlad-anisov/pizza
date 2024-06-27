from odoo import models
from odoo.http import request
import json


class ProductCartMixin(models.AbstractModel):
    _name = "product.cart.mixin"

    def add_to_cart(self):
        self.ensure_one()
        cart = json.loads(request.httprequest.cookies.get("cart", "[]"))
        if not any(x["product_id"] == self.id and x["product_model"] == self._name for x in cart):
            cart.append({
                "product_id": self.id,
                "product_model": self._name,
                "count": 1,
            })
        else:
            for line in cart:
                if line["product_id"] == self.id and line["product_model"] == self._name:
                    line["count"] += 1
        request.future_response.set_cookie("cart", json.dumps(cart))
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'title': "Добавлено:",
                'message': f"{self.name}",
                'next': {
                    'type': 'ir.actions.act_window_close'
                },
            }
        }
