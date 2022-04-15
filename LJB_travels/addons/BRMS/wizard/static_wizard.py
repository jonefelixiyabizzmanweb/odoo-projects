from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import date

class Reservation(models.TransientModel):
    _name = 'reservation.report'
    _description = "between dates"

    date_from = fields.Date(string="Date From", required=True)
    date_to = fields.Date(string="Date To", required=True)
    # code_id = fields.Many2many('reservation.details','Reservation id')


    def print_reservation(self):
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model')
        data['form'] = self.read(['date_from', 'date_to'])[0]
        print(data)
        return self.env.ref('brms.reservation_report').report_action([], data=data)
