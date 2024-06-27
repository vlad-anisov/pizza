from odoo import models, api
from jinja2 import Environment


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def get_view(self, view_id=None, view_type='form', **options):
        res = super().get_view(view_id, view_type, **options)
        if view_type != 'form':
            return res

        templater = Environment(variable_start_string="{{{", variable_end_string="}}}")
        record_id = self.browse(self.env.context.get("params", {}).get("id"))
        if self._name == "pizza.main.page":
            record_id = self.search([], limit=1)
        res["arch"] = templater.from_string(res["arch"]).render(record=record_id)

        return res