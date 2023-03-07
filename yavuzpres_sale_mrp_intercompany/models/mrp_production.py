from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    sale_order_line_id = fields.Many2one(
        comodel_name="sale.order.line",
        string="Source Sale Order Line",
    )

    sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Source Sale Order",
    )

    client = fields.Char(
        string='Customer',
    )

    parent_client = fields.Char(
        string='Teknotel Customer',
    )

    parent_client_ref = fields.Char(
        string='Teknotel Customer Purchase No',
    )

    date_source_order = fields.Date(
        string='Source Order Date',
    )
