from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import date

class CreateAmountWizard(models.TransientModel):
    _name = 'create.amount.wizard'
    _description ="create amount wizard"

    bus_name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code",required=True)

    def action_create_amount(self):
        print('aaa')

