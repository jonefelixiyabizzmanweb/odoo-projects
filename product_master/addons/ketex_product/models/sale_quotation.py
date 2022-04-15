from odoo import models, fields, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id),('creditor', '=', 'Creditor')]", )

    # product_code1 = fields.Many2one('ketex.product', "Product Code")

    test = fields.Many2many('ketex.product',string='Product Code')

    @api.onchange('test')
    def onchange_test(self):
        for rec in self:

            lines = [(5, 0, 0)]
            # for line in self.order_line:
            val = {
                'product_code': rec.test.id,
                'name': rec.test.description,
                'price_unit': rec.test.rate,
                'product_id': rec.test.product_id1,
            }
            lines.append((0, 0, val))

        print("lines", lines)
        rec.order_line = lines


class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # def _default_product_id(self):
    #     product_id = self.env['product.product'].search([('name', '=', 'Ketex')], limit=1).id
    #     return product_id

    product_code = fields.Many2one('ketex.product', "Product Code")

    name = fields.Text(string='Description', required=False)


class SaleOrderLineInherit(models.Model):
    _inherit = 'account.move.line'

    product_code = fields.Many2one('ketex.product', "Product Code", related="sale_line_ids.product_code")

