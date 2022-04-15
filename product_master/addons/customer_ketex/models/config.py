from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class CustomerType(models.Model):
    _name = "customer.type"
    _description = "Customer Type"
    _rec_name = "name"

    name = fields.Char(string='Name')

