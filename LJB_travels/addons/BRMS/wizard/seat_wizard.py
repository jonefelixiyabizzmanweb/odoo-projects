from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import date

class SeatWizard(models.TransientModel):
    _name = 'reservation.seat.wizard'


    day = fields.Date(string="Day ", required=True)


    def print_reservation(self):
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model')
        data['form'] = self.read(['day'])[0]
        print(data)
        return self.env.ref('brms.reservation_seat_report').report_action([], data=data)
