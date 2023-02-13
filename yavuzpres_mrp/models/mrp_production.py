from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    qty_produced = fields.Float(
        'Produced Quantity', store=True)
    qty_remaining = fields.Float(
        'Quantity To Be Produced', compute='_compute_qty_remaining', store=True)

    @api.depends('product_qty', 'qty_produced')
    def _compute_qty_remaining(self):
        for prop in self:
            prop.qty_remaining = (prop.product_qty - prop.qty_produced)
