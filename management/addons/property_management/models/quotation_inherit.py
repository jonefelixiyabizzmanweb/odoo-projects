from odoo import api, fields, models, _, SUPERUSER_ID

class Quotation(models.Model):
    _inherit = 'sale.order'
    
    
    # agent = fields.Many2one('res.users',"Agent/Broker")
    
class saleorderlineinherit(models.Model):
    _inherit = 'sale.order.line'    
    
    
    _sql_constraints = [
        ('accountable_required_fields',
            "check(1=1)",
            ".."),
        ('non_accountable_null_fields',
            "CHECK(display_type IS NULL OR (product_id IS NULL AND price_unit = 0 AND product_uom_qty = 0 AND product_uom IS NULL AND customer_lead = 0))",
            "Forbidden values on non-accountable sale order line"),
    ]
    
    def _default_product_id(self):
        return self.env['product.product'].search([('name', '=', 'property')], limit=1).id
    
    project = fields.Many2one('project.details',"Project",required=True)
    block = fields.Many2one('block',string="Block",domain="['|', ('project', '=', False), ('project', '=', project)]")
    flat_no = fields.Many2one('flat',"Flat.No",domain="['|',('building_block', '=', block),('building_block', '=', False)]")
    bhk = fields.Char(string="BHK")
    level = fields.Many2one('res.users',"Level")
    location = fields.Many2one('location.details',string="Location")
    # product_id = fields.Many2one('agent.form', string='project')
    area_sq = fields.Float(string="Qty")
    # rate_per = fields.Float(string="Rate",required=True)
    currency_id = fields.Many2one(related='product_id.currency_id', depends=['product_id.currency_id'], store=True, string='Currency', readonly=True)
    name = fields.Text(string='Description', required=True,default=".")
    types = fields.Selection([('1','Commercial'),('2','Residential')],string="Type")
    amenities = fields.Many2one('amenities.form',string='Amenities')
    uom = fields.Many2one('uom.uom',string="UoM")
    product_id = fields.Many2one(
        'product.product', string='Product', domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        change_default=True, ondelete='restrict', check_company=True,default=_default_product_id)
        
        
      
     # def _prepare_invoice(self):
        # invoice_vals = super(saleorderlineinherit, self)._prepare_invoice()
        # invoice_vals['project'] = self.project.id  or False
        # return invoice_vals
    # @api.multi
    # def _prepare_invoice_line(self, quantity):
        # res = super(saleorderlineinherit, self)._prepare_invoice_line(quantity)
        # res.update({'project': self.project})
        # return res
    
    
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
        

        
        
class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    
    