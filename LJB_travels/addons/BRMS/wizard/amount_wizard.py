from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import date

class ReservationAmountWizard(models.TransientModel):
    _name = 'reservation.amount.wizard'
    _description = "collected amount"

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)

    def print_reservation(self):
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model')
        data['form'] = self.read(['date_from', 'date_to'])[0]
        print(data)
        return self.env.ref('brms.reservation_amount_report').report_action([], data=data)
