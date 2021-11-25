# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class MergePickingWizard(models.TransientModel):
    _name = "mrp.merge.picking.wizard"

    is_merge_pick = fields.Boolean(string="Merge Picking")
    is_two_steps = fields.Boolean(string="Multi Steps")

    @api.model
    def default_get(self, fields):
        res = super(MergePickingWizard, self).default_get(fields)
        production_ids = self.env['mrp.production'].browse(self.env.context.get('active_ids', []))
        for production in production_ids:
            if not res.get('is_two_steps'):
                warehouse = production.location_src_id.get_warehouse().id
                if warehouse:
                    warehouse_id = self.env['stock.warehouse'].browse(warehouse)
                    if warehouse_id and not warehouse_id.manufacture_steps == 'mrp_one_step':
                        res['is_two_steps'] = True
        return res

    def get_procurement_id(self, production_ids):
        name = ", ".join([production.name for production in production_ids])
        procurement_id = self.env["procurement.group"].create({'name' : name}).id
        return procurement_id

    def confirmed_mrp_order(self):
        production_ids = self.env['mrp.production'].browse(self.env.context.get('active_ids', []))
        if not all(rec.state == 'draft' for rec in production_ids):
            raise ValidationError(_('Please select only draft production orders !'))
        procurement_id = self.get_procurement_id(production_ids)
        if self.is_merge_pick and self.is_two_steps:
            for rec in production_ids:
                rec.procurement_group_id = procurement_id
                rec.move_raw_ids.write({'group_id' : procurement_id})
                rec.action_confirm()

