from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class CustomerKetex(models.Model):
    _inherit = "res.partner"

    creditor = fields.Selection([('Creditor', 'Creditor'), ('Debitor', 'Debitor')], string="Debitor/Creditor",inverse='_inverse_state')
    contact_person = fields.Char(string="Contact Person")
    customer_type = fields.Many2one('customer.type', string="Customer Type")
    tds = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="TDS")
    tds_1 = fields.Char(string="TDS No")
    country_id = fields.Many2one('res.country', string="Location")
    tcs = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="TCS")
    tcs_1 = fields.Char(string="TCS No")
    state_id = fields.Many2one('res.country.state', string="State")
    cr = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="10 Cr")
    distance = fields.Integer(string="Distance From KGP")

    distance_unit = fields.Selection([('Kms','kms')],default="Kms",readonly=True)

    cus_ref = fields.Char(string='CUS Reference', required=True, copy=False, readonly=True,
                          default=lambda self: _('New'))
    creditor1 = fields.Selection([('C', 'C'), ('D', 'D')],default='C')
    cus_ref1 = fields.Char(compute="comp_name")


    def _inverse_state(self):
        if self.creditor == 'Creditor':
            return self.write({"creditor1": "C"})
        elif self.creditor == 'Debitor':
            return self.write({"creditor1": "D"})

    @api.model
    def create(self, vals):
        if vals.get('cus_ref', _('New')) == _('New'):
            vals['cus_ref'] = self.env['ir.sequence'].next_by_code('customer_ketex.seq') or _('New')

        result = super(CustomerKetex, self).create(vals)
        return result

    @api.depends('cus_ref','creditor1')
    def comp_name(self):
        for rec in self:
            cus2 = self.name
            cus3 = cus2[:1]
            rec.cus_ref1 = "%s%s%s" % \
               (rec.creditor1,cus3,rec.cus_ref)

