from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    intercompany_destination = fields.Boolean(
        string="Intercompany Destination",
    )
