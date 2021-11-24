from odoo import api, fields, models


class ManufacturingOrder(models.Model):
    _inherit = "mrp.production"

    def action_reset_draft(self):
        self.move_raw_ids.unlink()
        self.move_finished_ids.unlink()
        self.workorder_ids.unlink()
        self.write({'state': 'draft'})
        self._onchange_move_raw()
        return True


