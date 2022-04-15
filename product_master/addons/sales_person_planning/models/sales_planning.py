from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr



import math
import base64


class SalesPlanning(models.Model):
    _name = "sales.planning"
    _description = "Sales Planning"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "order_reference"


    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    role_id = fields.Many2many('sales.role', string="Role")
    location_id = fields.Many2one('sales.location', string="Location")
    start_datetime = fields.Date(string="Start Date")
    end_datetime = fields.Date(string="End Date")
    tag_ids = fields.Many2many('color.details', string="Tags")
    allocated_hours = fields.Float(string="Allocated Hours")
    repeat = fields.Boolean(string="Repeat")
    description = fields.Text(string="Note")
    conveyance = fields.Integer(string="Convenience")
    sequence = fields.Integer(string="Sequence", default=1,
                                  help="The order in which distribution lines are displayed and matched.")
    color = fields.Char(
            string="Color",
            help="Choose your color"
        )
    order_reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    state = fields.Selection([('0', 'None'), ('1', 'GG'), ('2', 'YY')],
                             string="Ribbon", default='0')





    @api.model
    def create(self, vals):
        if vals.get('order_reference', _('New')) == _('New'):
            vals['order_reference'] = self.env['ir.sequence'].next_by_code('sales_person_planning.sales.planning') or _('New')
            res = super(SalesPlanning, self).create(vals)
            return res

    def button_create(self):
        view_id = self.env.ref('crm.quick_create_opportunity_form')
        self.write({"state": "1"})

        result = {
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_type': 'tree',
            'view_mode': 'form',
            'target': 'new',
            # 'res_id': j.id,
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            # 'context': {'default_flat_ids': flatdetails}

        }
        return result
        # % (crm.crm_lead_lost_action)
        # d
    #
    # def action_lost_reason_apply(self):
    #     result = super(SalesPlanning, self).action_lost_reason_apply()
    #     self.env['sales.planning'].browse(self._context.get("active_ids")).update({"state": "2"})
    #     # self.write({"state": "2"})
    #     return result
    def button_lost(self):
        view_id = self.env.ref('sales_person_planning.second_warning_wizard')
        # self.write({"state": "2"})

        result = {
            'type': 'ir.actions.act_window',
            'res_model': 'lost.wizard',
            'view_type': 'tree',
            'view_mode': 'form',
            'target': 'new',
            # 'res_id': j.id,
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            # 'context': {'default_flat_ids': flatdetails}

        }
        return result



class Crm(models.Model):
    _inherit = "crm.lead"



