# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models
from odoo.osv import expression


class PricelistItem(models.Model):
    _name = "product.pricelist.item"
    _inherit = ["product.pricelist.item", "se.product.update.mixin"]

    def get_products(self):
        domains = [rec._se_get_product_domain() for rec in self]
        Products = self.env["product.product"]
        return Products.search(expression.OR(domains))

    def _se_get_product_domain(self):
        self.ensure_one()
        domain = []
        # TODO: confirm all-product case
        if self.applied_on == "3_global":
            return domain
        elif self.applied_on == "0_product_variant":
            domain.append(("id", "=", self.product_id.id))
        elif self.applied_on == "1_product":
            domain.append(("id", "in", self.product_tmpl_id.product_variant_ids.ids))
        elif self.applied_on == "2_product_category":
            domain.append(("product_tmpl_id.categ_id", "child_of", self.categ_id.id))
        return domain
