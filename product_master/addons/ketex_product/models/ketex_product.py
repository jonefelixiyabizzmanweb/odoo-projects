# -*- coding: utf-8 -*-

from odoo import models, fields, api


ACCOUNT_DOMAIN = "['&', '&', '&', ('deprecated', '=', False), ('internal_type','=','other'), ('company_id', '=', current_company_id), ('is_off_balance', '=', False)]"



class ketex_product(models.Model):
    _name = 'ketex.product'
    _rec_name = 'product_code'

    @api.model
    def _get_buy_route(self):
        buy_route = self.env.ref('purchase_stock.route_warehouse0_buy', raise_if_not_found=False)
        if buy_route:
            return buy_route.ids
        return []

    def _get_default_category_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('product.product_category_all')

    combination_name = fields.Many2one('ketex.config9', string="Combination Name")
    bool0 = fields.Boolean("Field 1 ",related="combination_name.bool0",readonly=False)
    field1 = fields.Many2one('ketex.config1',string="Field #1",related="combination_name.field1",readonly=False)
    bool1 = fields.Boolean("Field 2 ",related="combination_name.bool1",readonly=False)
    abb1 = fields.Char('ketex.config9',related="combination_name.abb1",readonly=False)
    field2 = fields.Many2one('ketex.config2',string="Field #2",related="combination_name.field2",readonly=False)
    bool2 = fields.Boolean("Field 3",related="combination_name.bool2",readonly=False)
    abb2 = fields.Char('ketex.config9',related="combination_name.abb2",readonly=False)
    field3 = fields.Many2one('ketex.config3',string="Field #3",related="combination_name.field3",readonly=False)
    bool3 = fields.Boolean("Variety",related="combination_name.bool3",readonly=False)
    abb3 = fields.Char('ketex.config9',related="combination_name.abb3",readonly=False)
    gauntlet_variety = fields.Many2one('ketex.config4',string="Variety",related="combination_name.gauntlet_variety",readonly=False)
    abb4 = fields.Char('ketex.config4',related="combination_name.abb4",readonly=False)
    bool4 = fields.Boolean("Type",related="combination_name.bool4",readonly=False)
    laterial_type = fields.Many2one('ketex.config5',string="Type",related="combination_name.laterial_type",readonly=False)
    bool5 = fields.Boolean("Edge wall",related="combination_name.bool5",readonly=False)
    edge_wall = fields.Many2one('ketex.config6',string="Edge Wall",related="combination_name.edge_wall",readonly=False)
    dia = fields.Float("Dia(mm)",related="combination_name.dia",readonly=False)
    panel = fields.Integer("Panel",related="combination_name.panel",readonly=False)
    height = fields.Float("Height(mm)",related="combination_name.height",readonly=False)
    tubes = fields.Integer("Tubes",related="combination_name.tubes",readonly=False)
    pitch = fields.Float("Pitch",related="combination_name.pitch",readonly=False)
    product_code = fields.Char("Product Code")
    description = fields.Char("Name")
    desc1 = fields.Text("Extra Description")
    link_old = fields.Char("Link Old Product Code")
    link_base = fields.Char("Link Base Product Code")
    ttwr = fields.Float("Text/Twist/Wind Rate(Rs.)")
    rate = fields.Float("Rate(Rs.)")
    category = fields.Many2one('product.category', "Category")
    unit = fields.Many2one('uom.uom',"Unit")
    chapter_head = fields.Char("Chapter Head")
    bool6 = fields.Boolean("Dia",related="combination_name.bool6")
    bool7 = fields.Boolean("Panel",related="combination_name.bool7")
    bool8 = fields.Boolean("Height",related="combination_name.bool8")
    bool9 = fields.Boolean("Tubes",related="combination_name.bool9")
    bool10 = fields.Boolean("Pitch",related="combination_name.bool10")
    bool11 = fields.Boolean("9/10",related="combination_name.bool11")
    absent = fields.Many2one('ketex.config8', related="combination_name.absent",readonly=False)

    description_sale = fields.Text(
        'Sales Description', translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")
    invoice_policy = fields.Selection([
        ('order', 'Ordered quantities'),
        ('delivery', 'Delivered quantities')], string='Invoicing Policy',
        help='Ordered Quantity: Invoice quantities ordered by the customer.\n'
             'Delivered Quantity: Invoice quantities delivered to the customer.',
        default='order')
    expense_policy = fields.Selection(
        [('no', 'No'), ('cost', 'At cost'), ('sales_price', 'Sales price')],
        string='Re-Invoice Expenses',
        default='no',
        help="Expenses and vendor bills can be re-invoiced to a customer."
             "With this option, a validated expense can be re-invoice to a customer at its cost or sales price.")
    # seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id', 'Vendors', depends_context=('company',),
                                 # help="Define vendor pricelists.")
    # supplier_taxes_id = fields.Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id',
                                         # string='Vendor Taxes', help='Default taxes used when buying the product.',
                                         # domain=[('type_tax_use', '=', 'purchase')],
                                         # default=lambda self: self.env.company.account_purchase_tax_id)
    # purchase_method = fields.Selection([
    #     ('purchase', 'On ordered quantities'),
    #     ('receive', 'On received quantities'),
    # ], string="Control Policy", help="On ordered quantities: Control bills based on ordered quantities.\n"
    #                                  "On received quantities: Control bills based on received quantities.",
    #     default="receive")
    # description_purchase = fields.Text(
    #     'Purchase Description', translate=True)
    route_ids = fields.Many2many(default=lambda self: self._get_buy_route())
    responsible_id = fields.Many2one(
        'res.users', string='Responsible', default=lambda self: self.env.uid, company_dependent=True,
        check_company=True,
        help="This user will be responsible of the next activities related to logistic operations for this product.")
    volume = fields.Float(
        'Volume', digits='Volume', store=True)
    # volume_uom_name = fields.Char(string='Volume unit of measure label')
    weight = fields.Float(
        'Weight',  digits='Stock Weight',
         store=True)
    # weight_uom_name = fields.Char(string='Weight unit of measure label')
    sale_delay = fields.Float(
        'Customer Lead Time', default=0,
        help="Delivery lead time, in days. It's the number of days, promised to the customer, between the confirmation of the sales order and the delivery.")
    produce_delay = fields.Float(
        'Manufacturing Lead Time', default=0.0,
        help="Average lead time in days to manufacture this product. In the case of multi-level BOM, the manufacturing lead times of the components will be added.")
    tracking = fields.Selection([
        ('serial', 'By Unique Serial Number'),
        ('lot', 'By Lots'),
        ('none', 'No Tracking')], string="Tracking",
        help="Ensure the traceability of a storable product in your warehouse.", default='none', required=True)
    property_stock_production = fields.Many2one(
        'stock.location', "Production Location",
        help="This stock location will be used, instead of the default one, as the source location for stock moves generated by manufacturing orders.")
    
    property_stock_inventory = fields.Many2one(
        'stock.location', "Inventory Location",
       help="This stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory.")
    description_pickingout = fields.Text('Description on Delivery Orders', translate=True)
    description_pickingin = fields.Text('Description on Receptions', translate=True)
    property_account_income_id = fields.Many2one('account.account', company_dependent=True,
                                                 string="Income Account",
                                                
                                                 help="Keep this field empty to use the default value from the product category.")
    property_account_expense_id = fields.Many2one('account.account', company_dependent=True,
                                                  string="Expense Account",
                                                  
                                                  help="Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.")

    asset_category_id = fields.Many2one('account.asset.category', string='Asset Type',
                                        company_dependent=True, ondelete="restrict")
    property_account_creditor_price_difference = fields.Many2one(
        'account.account', string="Price Difference Account", company_dependent=True,
        help="This account is used in automated inventory valuation to " \
             "record the price difference between a purchase order and its related vendor bill when validating this vendor bill.")

    # other information

    type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='consu', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    categ_id = fields.Many2one(
        'product.category', 'Product Category',
        change_default=True, default=_get_default_category_id, group_expand='_read_group_categ_id',
        required=True, help="Select category for the current product")
    barcode = fields.Char('Barcode')
    # , compute = '_compute_barcode', inverse = '_set_barcode', search = '_search_barcode'
    default_code = fields.Char(
        'Internal Reference')
        # compute='_compute_default_code',
        # inverse='_set_default_code', store=True)
    list_price = fields.Float(
        'price', default=1.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.")
    company_id = fields.Many2one(
        'res.company', 'Company', index=1)
    standard_price = fields.Float(
        'Cost',help="""In Standard Price & AVCO: value of the product (automatically computed in AVCO).
           In FIFO: value of the last unit that left the stock (automatically computed).
           Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
           Used to compute margins on sale orders.""")

    tax_ids = fields.Many2many('account.tax',string='Customer Taxes')


    # @api.depends('abb1','abb2')
    def comp_name(self):
        for rec in self:
            product_code1 = (rec.abb1 or '')+'.'+(rec.abb2 or '')+'.'+(rec.abb3 or '')
            rec.product_code = "%s%0.2f%d%0.2f%d%0.2f" % \
                         (product_code1, rec.dia or 0.0,rec.panel or 0, rec.height or 0.0, rec.tubes or 0, rec.pitch or 0.0)

            rec.description = "%0.2f mm * %0.2f mm * %d  Tubes (%s)" % \
                                (rec.dia or 0.0,rec.height or 0.0, rec.tubes or 0,rec.abb4)


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    product = fields.Many2one('ketex.product',string='Product Code')