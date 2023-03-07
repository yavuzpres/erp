from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    intercompany_operation = fields.Boolean(
        string='Intercompany Sale Manufacturing',
    )
