from odoo import models, fields, api


class EmployeeWizard(models.TransientModel):
    _name = "employee.wizard"


    lost_reason_id = fields.Many2one('crm.lost.reason', 'Lost Reason')

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        self.env['by.employee'].browse(self._context.get("active_ids")).update({"state": "2"})
        return leads.action_set_lost(lost_reason=self.lost_reason_id.id)
