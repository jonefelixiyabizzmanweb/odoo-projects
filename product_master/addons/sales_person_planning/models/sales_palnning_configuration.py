from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


# class SalesEmployees(models.Model):
#     _name = "sales.employee"
#     _description = "Sales Employee"
#     _rec_name = "employee"
#
#     employee = fields.Char(string="Employees Name", required=True)
#     color = fields.Char(
#         string="Color",
#         help="Choose your color"
#     )
#     sequence = fields.Integer(string="Sequence", default=1,
#                               help="The order in which distribution lines are displayed and matched.")
#

class SalesLocation(models.Model):
    _name = "sales.location"
    _description = "Sales Location"
    _rec_name = "location"

    location = fields.Char(string="Location Name")
    street = fields.Char(string="Street1", required=True)
    street2 = fields.Char(string="Street2", required=True)
    city = fields.Char(string="City", required=True)
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    zip = fields.Char(string="Zip Code", required=True)
    sequence = fields.Integer(string="Sequence", default=1,
                              help="The order in which distribution lines are displayed and matched.")
    tag = fields.Char(string="Tags")

class SalesRole(models.Model):
    _name = "sales.role"
    _description = "Sales Role"
    _rec_name = "role_name"

    role_name = fields.Char(string="Role Name",required=True)
    employee = fields.Many2many('sales.employee', string="Employees Name")
    color = fields.Char(
        string="Color",
        help="Choose your color"
    )
    sequence = fields.Integer(string="Sequence", default=1,
                              help="The order in which distribution lines are displayed and matched.")

class Color(models.Model):
    _name = "color.details"
    _description = "color Details"
    _rec_name = "name"

    name = fields.Char(string='Name')
    color = fields.Char(string='Colors', help="Choose your color")


