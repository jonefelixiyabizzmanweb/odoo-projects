from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64

class RequestIndent(models.Model):
    _name = "request.indent"
    _description = "Request Indent"
    _rec_name = 'order_reference'

    def _default_user_id(self):
        user_id = self.env['res.users'].search([('name', '=', 'Mitchell Admin')], limit=1).id
        return user_id


    purpose = fields.Many2one('purpose', string="Purpose")
    cost_center = fields.Many2one('account.analytic.account', string="Cost Center")
    date = fields.Date(string="Date")
    shop_floor = fields.Many2one('floor.type', string="Shop Floor")
    user_id = fields.Many2one(
        'res.users', string='Created By', default=_default_user_id)
    altered_by = fields.Many2one(
            'res.users', string='Altered By', index=True, tracking=2,
            default=lambda self: self.env.user
            ,

            domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])

    description = fields.Html(string="Description")

    order_reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                                  default=lambda self: _('New'))

    request_indent_line_ids = fields.One2many('request.indent.line', 'request_ids', string='')

    users_id = fields.Many2one(
        'res.users', string='Purchase Representative', index=True, tracking=True,
        default=lambda self: self.env.user, check_company=True)
    incoterm_id = fields.Many2one('account.incoterms', 'Incoterm')
    invoice_status = fields.Selection([
        ('no', 'Nothing to Bill'),
        ('to invoice', 'Waiting Bills'),
        ('invoiced', 'Fully Billed'),
    ], string='Billing Status', store=True, readonly=True, copy=False, default='no')
    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms')
    fiscal_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position')


    state = fields.Selection([('draft','Draft'),('confirm', 'Purchase Order')],
                             string="Status")

    def action_confirm(self):
        self.state = 'confirm'

    @api.model
    def create(self, vals):
        if vals.get('order_reference', _('New')) == _('New'):
            vals['order_reference'] = self.env['ir.sequence'].next_by_code('request_for_indent.request.indent') or _(
                'New')
            res = super(RequestIndent, self).create(vals)
        return res


class Product(models.Model):
    _name = "request.indent.line"
    _description = "Request Indent Line"

    def _get_default_uom_id(self):
        return self.env.ref('uom.product_uom_unit')

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Char(string="Description")
    # name = fields.Text(string='Description', required=False)
    quantity = fields.Char(string="Quantity")
    uom_id = fields.Many2one(
        'uom.uom', 'Unit of Measure',
        default=_get_default_uom_id, required=True,
        help="Default unit of measure used for all stock operations.")

    request_ids = fields.Many2one('request.indent', string='Request')


class SaleOrderLineInherit(models.Model):
    _inherit = 'purchase.order'

    indent_no = fields.Many2one('request.indent',string="Indent No")

    @api.onchange('indent_no')
    def onchange_indent_no(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.indent_no.request_indent_line_ids:
                val = {
                    'product_id': line.product_id.id,
                    'name': line.product_id.description,
                    'product_qty': line.quantity,
                    'product_uom': line.uom_id,
                }

                lines.append((0, 0, val))

        print("lines", lines)
        rec.order_line = lines



class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"

    name = fields.Text(string='Description')
