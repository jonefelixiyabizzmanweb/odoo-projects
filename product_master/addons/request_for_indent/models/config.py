from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class Purpose(models.Model):
    _name = "purpose"
    _description = "Purpose"
    _rec_name = "purpose"

    purpose = fields.Char(string='Purpose')

class FloorType(models.Model):
    _name = "floor.type"
    _description = "Floor Type"
    _rec_name = "name"

    name = fields.Char(string='Floor Type')

