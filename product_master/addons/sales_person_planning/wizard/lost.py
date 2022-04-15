from odoo import models, fields, api


class LostWizard(models.TransientModel):
    _name = "lost.wizard"


    lost_reason_id = fields.Many2one('crm.lost.reason', 'Lost Reason')

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        self.env['sales.planning'].browse(self._context.get("active_ids")).update({"state": "2"})
        return leads.action_set_lost(lost_reason=self.lost_reason_id.id)

    # def action_lost_reason_apply(self):
    #     result = super(SalesPlanning, self).action_lost_reason_apply()
    #     self.env['sales.planning'].browse(self._context.get("active_ids")).update({"state": "2"})
    #     # self.write({"state": "2"})
    #     return result

    # reason = fields.Many2one('crm'string="Start Date")
    # end_date = fields.Date(string="End Date")
    #
    # def update_second(self):
    #     self.env['hr.warning'].browse(self._context.get("active_ids")).update({'start_date': self.start_date})
    #     self.env['hr.warning'].browse(self._context.get("active_ids")).update({'end_date': self.end_date})
    #     self.env['hr.warning'].browse(self._context.get("active_ids")).update({"state": "second_warning"})
    #     # template_id = self.env.ref('hr_warning.second_warning_mail').id
    #     # template = self.env['mail.template'].browse(template_id)
    #     # template.send_mail(self.id, force_send=True)
    #     return True