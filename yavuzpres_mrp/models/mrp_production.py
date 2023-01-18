from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    qty_produced = fields.Float(
        'Produced Quantity', store=True)
