from dateutil.relativedelta import relativedelta

from odoo import _, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    parent_client_ref = fields.Char(
        string='Teknotel Customer Purchase No',
    )

    def action_create_mo(self):
        self = self.sudo()
        dest_company_id = self.env['res.company'].search([
            ('intercompany_destination', '=', True)
        ], limit=1)
        if not dest_company_id:
            raise UserError(_('Inter-company destination not found!'))
        picking_type_id = self.env['stock.picking.type'].search([
            ('intercompany_operation', '=', True),
            ('company_id', '=', dest_company_id.id),
        ], limit=1)
        if not picking_type_id:
            raise UserError(_('Inter-company operation type not found!'))
        for order in self:
            for line in order.order_line.filtered(lambda l: not l.mo_id):
                bom_id = line.product_id.variant_bom_ids[0] if line.product_id.variant_bom_ids else line.product_id.bom_ids[0]
                if not bom_id:
                    continue
                if bom_id.company_id and bom_id.company_id != dest_company_id.id:
                    bom_id = bom_id.copy({'company_id': dest_company_id.id})
                mo_id = self.env['mrp.production'].create({
                    'sale_order_id': order.id,
                    'sale_order_line_id': line.id,
                    'product_id': line.product_id.id,
                    'product_uom_id': line.product_id.uom_id.id,
                    'bom_id': bom_id.id,
                    'product_qty': line.product_uom_qty,
                    'date_deadline': order.commitment_date - relativedelta(days=2) if order.commitment_date else False,
                    'user_id': False,
                    'company_id': dest_company_id.id,
                    'client': dest_company_id.name, #11 x_studio_musteri
                    'origin': order.client_order_ref, #12
                    'parent_client': order.partner_id.name, #13 x_studio_ust_musteri
                    'parent_client_ref': order.partner_id.ref, #14 x_studio_ust_musteri_referansi
                    'date_source_order': order.date_order, #16
                    'picking_type_id': picking_type_id.id,
                    'location_src_id': picking_type_id.default_location_src_id.id,
                    'location_dest_id': picking_type_id.default_location_dest_id.id,
                })
                mo_id._onchange_move_raw()
                line.mo_id = mo_id
