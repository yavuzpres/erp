from odoo import fields, models


class SaleImportProductsPricelist(models.TransientModel):
    _inherit = "sale.import.products"

    def _multi_add_price_list(self):
        saleorder_id = self.env['sale.order'].browse(self._context.get('active_id'))
        pricelist_id = saleorder_id.partner_id.property_product_pricelist
        product_ids = pricelist_id.item_ids.mapped('product_id')
        return [('id', 'in', product_ids.ids)] if pricelist_id else []

    product_ids = fields.Many2many(domain=_multi_add_price_list, )

