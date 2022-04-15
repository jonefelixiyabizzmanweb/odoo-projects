from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr


class ProductDetails(models.Model):
    # _name = 'product.details'
    # _description = 'product details'
    _inherit = 'product.template'
    _rec_name = "block"
    # _rec_name = "hsn_sac_code"

    # def name_get(self):
    #     res = []
    #     for data in self:
    #         res.append((data.id, str(data. name)))
    #     return res

    # def name_get(self):
    #     res = []
    #     for data in self:
    #         res.append((data.id, str(data.name) + ' - ' + str(data.block)))
    #     return res
    # name = fields.Char(string='Name')
    name = fields.Many2one('project.details',string='Name', index=True, required=True)
    hsn_sac_code = fields.Char(string="HSN/SAC Code")
    hsn_sac_description = fields.Char(string="HSN/SAC Description")
    unit_of_measure = fields.Many2one('uom',string="Unit of Measure")
    purchase_unit_of_measure = fields.Char(string="Purchase Unit of Measure")
    block = fields.Many2one('block',string="Block Name",domain="['|', ('project', '=', False), ('project', '=', name)]")
    # # location = fields.Many2one(string="Location", related="name.location")
    # flat_ids = fields.One2many('flat', 'flat_line_ids', string="")
    # # rate = fields.Float(string="Rate/Sq.ft")
    # project_rate = fields.Char(string="Rate/Sq.ft")

    # flat_name = fields.Many2one('flat',string='Flat Name/No')
    # area = fields.Many2one('flat',string="Area(SB) Sq.ft")
    # bhk = fields.Many2one('flat',string="BHK")
    # level = fields.Many2one('flat',string="Level")
    # total_amount = fields.Many2one('flat',string="Total(Rs)")


class Flat(models.Model):
    _name = "flat"
    _description = "flat basic Details"
    _rec_name = "flat_name"

    building_block = fields.Many2one('block', string="Block Name")
    flat_name = fields.Char(string='Flat Name/No')
    area = fields.Float(string="Area(SB) Sq.ft")
    bhk = fields.Char(string="BHK")
    level = fields.Char(string="Level")
    rate_per_sq = fields.Float(string="Rate/Sq.ft")
    total_amount = fields.Float(string="Total(Rs)",compute='compute_rate')
    flat_line_ids = fields.Many2one('product.template',string="Flate Line Id")
    # rate_per = fields.Float(string="Rate/Sq.ft",required=True)
    # taxes_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    # price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', store=True)
    # price_total = fields.Monetary(compute='_compute_amount', string='Total', store=True)
    # price_tax = fields.Float(compute='_compute_amount', string='Tax', store=True)
    # currency_id = fields.Many2one(related='product_id.currency_id', depends=['product_id.currency_id'], store=True, string='Currency', readonly=True)
    
    @api.depends('area', 'rate_per_sq')
    def compute_rate(self):
        for line in self:
            line.total_amount= line.area * line.rate_per_sq
            
            # vals = line._prepare_compute_all_values()
            # taxes = line.taxes_id.compute_all(
                # vals['rate_per'],
                # vals['currency_id'],
                # vals['area'],
                # # vals['product'],
                # vals['partner'])
            # line.update({
                # 'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                # 'price_total': taxes['total_included'],
                # 'price_subtotal': taxes['total_excluded'],
            # })