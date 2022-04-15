from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class PropertyDetails(models.Model):
    _name = "property.details"
    _description = "Property Details"
    _rec_name = "name"

    name = fields.Char('Reference No.', size=24, readonly=True, track_visibility='onchange',
                       default=lambda self: _('New'))
    street = fields.Char(string="Street1", required=True)
    street2 = fields.Char(string="Street2", required=True)
    city = fields.Char(string="City", required=True)
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    zip = fields.Char(sring="Zip", required=True)
    date = fields.Datetime(string="Date", default=lambda self: fields.Datetime.now(), required=True)
    # sale_order_id = fields.Many2one('sale.order', 'Sale order')
    flat_line_ids = fields.One2many('flat.details.lines', 'flat_ids', string='Property Lines')
    building_line_ids = fields.One2many('building.details.lines', 'building_ids', string='Building Details')
    video_url = fields.Char(string="Video URL")
    property_types = fields.Many2many('property.type', string='Property Type')
    property_name = fields.Char(string="Property Name")
    no_building = fields.Integer(string="No of Building")
    area = fields.Integer(string='Area in acres', required=True)
    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('property.details.seq') or _('New')
        return super(PropertyDetails, self).create(vals)

    def attachment_tree_view(self):
        action = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        action['domain'] = str([
            '&',
            ('res_model', '=', 'property.details'),
            ('res_id', 'in', self.ids),
        ])
        action['context'] = "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        return action

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'property.details'), ('res_id', '=', self.id),
            ])

    # def create_flat_so(self):
    #     create_so_line = []
    #
    #     new_sale_order = self.env['sale.order'].create({
    #         'partner_id': self.env.user.partner_id.id,
    #         'res_model': self._name,
    #     })
    #
    #     for line in self.flat_line_ids:
    #         print("---------------Active ID-------------------", line)
    #         create_so = self.env['sale.order.line'].create({
    #             'product_id': line.product_id.id,
    #             'name': line.product_id.name,
    #             'price_unit': line.sell_price,
    #             'product_uom_qty': 1,
    #             'order_id': new_sale_order.id,
    #         })
    #
    #         create_so_line.append(create_so)
    #         print("---------------SO Created-------------------", create_so.product_id, create_so.name,
    #               create_so.price_unit, create_so.order_id)
    #
    #     view_id = self.env.ref('sale.view_order_form')
    #     return {
    #         'name': _('New Sales Quotation'),
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'sale.order',
    #         'res_id': new_sale_order.id,
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #         'view_id': view_id.id,
    #         'views': [(view_id.id, 'form')],
    #         'context': {
    #             'default_order_line': create_so_line, 'default_state': 'draft', }
    #     }


class FlatDetailsLines(models.Model):
    _name = "flat.details.lines"
    _description = "Flat Details"

    product_id = fields.Many2one('product.product', string='Flat Name')
    product_qty = fields.Char(string='No of Kitchen')
    bathroom = fields.Char(string='No of Bathroom')
    hall = fields.Char(string='No of Hall')
    bedroom = fields.Char(string='No of Bedroom')
    carpet = fields.Integer(string='Carpet Area')
    facing = fields.Char(string='Facing')
    balcony = fields.Char(string='Balcony')
    furnishing = fields.Char(string='Furnishing')
    floor = fields.Char(string='Floor')
    sell_price = fields.Integer(string='Sell Price')
    brokerage_charge = fields.Integer(string='Brokerage Charge')
    state = fields.Selection(selection=[
        ('in_progress', 'In Progress'),
        ('occupied', 'Occupied'),
    ], string='Status')
    flat_ids = fields.Many2one('property.details', string='Property ID')

    def create_flat_so(self):
        create_so_line = []

        new_sale_order = self.env['sale.order'].create({
            'partner_id': self.env.user.partner_id.id,
            'res_model': self._name,
        })

        for line in self:
            print("---------------Active ID-------------------", line)
            create_so = self.env['sale.order.line'].create({
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'price_unit': line.sell_price,
                'product_uom_qty': 1,
                'order_id': new_sale_order.id,
            })

            create_so_line.append(create_so)
            print("---------------SO Created-------------------", create_so.product_id, create_so.name,
                  create_so.price_unit, create_so.order_id)

        view_id = self.env.ref('sale.view_order_form')
        return {
            'name': _('New Sales Quotation'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': new_sale_order.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            'context': {
                'default_order_line': create_so_line, 'default_state': 'draft', }
        }


class BuildingDetailsLines(models.Model):
    _name = "building.details.lines"
    _description = "Building Details"

    building_id = fields.Many2one('product.template', string='Building Name')
    no_flat = fields.Char(string='No of Flats')
    building_ids = fields.Many2one('property.details', string='Details ID')

    def create_building(self):
        create_building_line = []

        for line in self:
            print("---------------Active ID-------------------", line)
            create_building = (0, 0, {
                'name': line.id,
            })

            create_building_line.append(create_building)
            print("---------------Building Created-------------------", create_building)

        view_id = self.env.ref('product.product_template_only_form_view')
        return {
            'name': _('New Purchase Quotation'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            'context': {
                'default_order_line': create_building_line, }
        }
