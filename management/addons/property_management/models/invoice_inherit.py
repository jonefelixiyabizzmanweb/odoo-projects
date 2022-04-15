from odoo import api, fields, models, _, SUPERUSER_ID


class saleorderlineinherit(models.Model):
    _inherit = 'account.move.line'
    
    
    # def _default_product_id(self):
        # return self.env['account.move'].search([('project', '=', project.id)], limit=1).id

    # area_sq = fields.Float(string="Qty")
    # rate_per = fields.Float(string="Rate",required=True)
    flat_no = fields.Many2one('flat',"Flat.No",related="sale_line_ids.flat_no")
    uom = fields.Many2one('uom.uom',"UoM",related="sale_line_ids.uom")
    project = fields.Many2one('project.details',"Project",required=True,related="sale_line_ids.project")
    block = fields.Many2one('block',string="Block",domain="['|', ('project', '=', False), ('project', '=', project)]",related="sale_line_ids.block")
    bhk = fields.Char(string="BHK",related="sale_line_ids.bhk")
    level = fields.Many2one('res.users',"Level")
    location = fields.Many2one('location.details',string="Location",related="sale_line_ids.location")
    amenities = fields.Many2one('amenities.form',string='Amenities',related="sale_line_ids.amenities")
    types = fields.Selection([('1','Commercial'),('2','Residential')],string="Type",related="sale_line_ids.types")
    
    
class invoiceorderlineInherit(models.Model):
    _inherit = 'account.move'
    
    
    
    project = fields.Many2one('project.details',"Project",required=True)
    flat_no = fields.Many2one('flat',"Flat.No")
    block = fields.Many2one('block',string="Block",domain="['|', ('project', '=', False), ('project', '=', project)]")
    bhk = fields.Char(string="BHK")
    level = fields.Many2one('res.users',"Level")
    location = fields.Many2one('location.details',string="Location")
    types = fields.Selection([('1','Commercial'),('2','Residential')],string="Type")
    
    
    # @api.onchange('project')
    # def _onchange_state_pro(self):
        # for rec in self:
            # lines = []
            # for line in self.quantity:
                # val = {
                    # 'project': self.project.id ,
                    # 'block': self.block.id,
                    # 'flat_no': self.flat_no.id,
                    # 'bhk':self.bhk,
                    # # 'price_unit':self.rate_per_sq,
                    # # 'product_uom_qty':self.area_sq,
                    # 'location':self.location.id,
                    # # 'amenities':self.amenities.id,
                    # # 'product_id': 'property',
                    # # 'product_uom':self.uom.id,
                    # }
                # lines.append((0,0,val))
            # rec.invoice_line_ids = lines
    # @api.depends('area_sq', 'rate_per', 'tax_id')
    # def _compute_amount(self):
        # for line in self:
            # vals = line._prepare_compute_all_values()
            # taxes = line.tax_id.compute_all(
                # vals['rate_per'],
                # vals['currency_id'],
                # vals['area_sq'],
                # vals['product'],
                # vals['partner'])
            # line.update({
                # 'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                # 'price_total': taxes['total_included'],
                # 'price_subtotal': taxes['total_excluded'],
            # })
            
    # def _prepare_compute_all_values(self):
        # self.ensure_one()
        # return {
            # 'rate_per': self.rate_per,
            # 'currency_id': self.order_id.currency_id,
            # 'area_sq': self.area_sq,
            # 'product': self.product_id,
            # 'partner': self.order_id.partner_id,
        # }
        
    # def _get_price_total_and_subtotal_model(self, rate_per, area_sq, discount, currency, product, partner, taxes, move_type):
        # ''' This method is used to compute 'price_total' & 'price_subtotal'.

        # :param price_unit:  The current price unit.
        # :param quantity:    The current quantity.
        # :param discount:    The current discount.
        # :param currency:    The line's currency.
        # :param product:     The line's product.
        # :param partner:     The line's partner.
        # :param taxes:       The applied taxes.
        # :param move_type:   The type of the move.
        # :return:            A dictionary containing 'price_subtotal' & 'price_total'.
        # '''
        # res = {}

        # # Compute 'price_subtotal'.
        # line_discount_price_unit = rate_per * (1 - (discount / 100.0))
        # subtotal = area_sq * line_discount_price_unit

        # # Compute 'price_total'.
        # if taxes:
            # force_sign = -1 if move_type in ('out_invoice', 'in_refund', 'out_receipt') else 1
            # taxes_res = taxes._origin.with_context(force_sign=force_sign).compute_all(line_discount_price_unit,
                # area_sq=area_sq, currency=currency, product=product, partner=partner, is_refund=move_type in ('out_refund', 'in_refund'))
            # res['price_subtotal'] = taxes_res['total_excluded']
            # res['price_total'] = taxes_res['total_included']
        # else:
            # res['price_total'] = res['price_subtotal'] = subtotal
        # #In case of multi currency, round before it's use for computing debit credit
        # if currency:
            # res = {k: currency.round(v) for k, v in res.items()}
        # return res