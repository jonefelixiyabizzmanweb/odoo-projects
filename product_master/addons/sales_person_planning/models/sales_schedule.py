from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64



class ByEmployee(models.Model):
    _name = "by.employee"
    _description = "By Employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "reference"

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    role_id = fields.Many2many('sales.role', string="Role")
    location_id = fields.Many2one('sales.location', string="Location")
    start_datetime = fields.Date(string="Start Date")
    end_datetime = fields.Date(string="End Date")
    tag_ids = fields.Many2many('color.details', string="Tags")
    allocated_hours = fields.Float(string="Allocated Hours")
    repeat = fields.Boolean(string="Repeat")
    description = fields.Text(string="Additional Note")
    conveyance = fields.Integer(string="Convenience")


    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    state = fields.Selection([('0', 'None'), ('1', 'GG'), ('2', 'YY')],
                             string="Ribbon", default='0')

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('sales_person_planning.by.employee') or _('New')
            res = super(ByEmployee, self).create(vals)
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

    def button_lost(self):
        view_id = self.env.ref('sales_person_planning.second_warning_wizard')
        # self.write({"state": "2"})

        result = {
            'type': 'ir.actions.act_window',
            'res_model': 'employee.wizard',
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
class ByRole(models.Model):
    _name = "by.role"
    _description = "By Role"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "code"

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    role_id = fields.Many2one('sales.role', string="Role")
    location_id = fields.Many2one('sales.location', string="Location")
    start_datetime = fields.Date(string="Start Date")
    end_datetime = fields.Date(string="End Date")
    tag_ids = fields.Many2many('color.details', string="Tags")
    allocated_hours = fields.Float(string="Allocated Hours")
    repeat = fields.Boolean(string="Repeat")
    description = fields.Text(string="Additional Note")
    conveyance = fields.Integer(string="Convenience")


    code = fields.Char(string='Order', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    state = fields.Selection([('0', 'None'), ('1', 'GG'), ('2', 'YY')],
                             string="Ribbon", default='0')


    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('sales_person_planning.by.role') or _('New')
            res = super(ByRole, self).create(vals)
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

    def button_lost(self):
        view_id = self.env.ref('sales_person_planning.second_warning_wizard')
        # self.write({"state": "2"})

        result = {
            'type': 'ir.actions.act_window',
            'res_model': 'role.wizard',
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


