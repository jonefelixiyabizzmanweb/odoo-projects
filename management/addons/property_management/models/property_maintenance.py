from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class PropertySales(models.Model):
    _inherit = "sale.order"

    res_model = fields.Char(string="Resource Model")


class PropertyMaintenance(models.Model):
    _name = "property.maintenance"
    _description = "Property Maintenance"

    name = fields.Char('Reference No.', size=24, readonly=True, track_visibility='onchange',
                       default=lambda self: _('New'))
    build_and_flat_number = fields.Many2one('product.product', string="Building and Flat No.")
    flat_no = fields.Integer(string="Flat Number")
    issue_date = fields.Datetime(string="Issued On", default=lambda self: fields.Datetime.now(), readonly=True)
    document = fields.Binary(string="Attachment")
    issues = fields.Html(string='Issues')
    state = fields.Selection(selection=[
        ('new', 'New'),
        ('ongoing', 'Ongoing'),
        ('resolved', 'Resolved'),
    ], default="new", string='Status')

    # @api.multi
    def make_to_new(self):
        return self.write({'state': 'new'})

    # @api.multi
    def mark_ongoing(self):
        return self.write({'state': 'ongoing'})

    # @api.multi
    def mark_resolved(self):
        return self.write({'state': 'resolved'})

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('property.maintenance.seq') or _('New')
        return super(PropertyMaintenance, self).create(vals)

    def attachment_tree_view(self):
        action = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        action['domain'] = str([
            '&',
            ('res_model', '=', 'property.maintenance'),
            ('res_id', 'in', self.ids),
        ])
        action['context'] = "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        return action

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'property.maintenance'), ('res_id', '=', self.id),
            ])


class PreventiveMaintenance(models.Model):
    _name = "preventive.maintenance"
    _description = "Preventive Maintenance"

    name = fields.Char('Reference No.', size=24, readonly=True, track_visibility='onchange',
                       default=lambda self: _('New'))

    build_and_flat_number = fields.Many2one('product.product', string="Building and Flat Number")
    issue_date = fields.Datetime(string="Issued On", default=lambda self: fields.Datetime.now(), readonly=True)
    amc_validity = fields.Many2one('amc.validity', string="AMC Validity")
    contract_expiry_date = fields.Date(string="Contract Expiry Date", compute="compute_expiry_date", readonly=True)
    repairing_period = fields.Many2one('repairing.period', string="Repairing Period")
    service_line_ids = fields.One2many('service.charge.lines', 'service_charge_ids',
                                       string="Service Charge")
    maintenance_line_ids = fields.One2many('preventive.maintenance.lines', 'maintenance_ids',
                                           string="Maintenance Date Schedule")
    doc_count = fields.Integer(compute='_compute_attached_docs_count', string="Number of documents attached")

    @api.onchange('repairing_period')
    def compute_maintenance_lines(self):
        if self.repairing_period:
            self.maintenance_line_ids = False
        # else:
        #     self.maintenance_line_ids = True

    @api.onchange('amc_validity')
    def compute_expiry_date(self):
        if int(self.amc_validity) == 1:
            print("**********************************", int(self.amc_validity))
            self.contract_expiry_date = self.issue_date + relativedelta(years=int(self.amc_validity))

        elif int(self.amc_validity) == 2:
            print("**********************************", int(self.amc_validity))
            self.contract_expiry_date = self.issue_date + relativedelta(years=int(self.amc_validity))

        elif int(self.amc_validity) == 3:
            print("**********************************", int(self.amc_validity))
            self.contract_expiry_date = self.issue_date + relativedelta(years=int(self.amc_validity))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('preventive.maintenance.seq') or _('New')
        return super(PreventiveMaintenance, self).create(vals)

    def attachment_tree_view(self):
        action = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        action['domain'] = str([
            '&',
            ('res_model', '=', 'preventive.maintenance'),
            ('res_id', 'in', self.ids),
        ])
        action['context'] = "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        return action

    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
                '&',
                ('res_model', '=', 'preventive.maintenance'), ('res_id', '=', self.id),
            ])

    def create_renewal_wizard_action(self):
        view_id = self.env.ref('property_management.create_renewal_form')
        return {
            'name': _('AMC Renewal Form'),
            'type': 'ir.actions.act_window',
            'res_model': 'amc.renewal',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            'context': {
                'default_build_and_flat_number': self.build_and_flat_number.id, 'default_reference_no': self.name, }
        }


class PreventiveMaintenanceLines(models.Model):
    _name = "preventive.maintenance.lines"
    _description = "Preventive Maintenance Lines"

    maintenance_ids = fields.Many2one("preventive.maintenance", string="Maintenance ID")
    maintenance_date = fields.Datetime(string="Maintenance Date", required=True,
                                       default=lambda self: fields.Datetime.now())
    description = fields.Text(string="Description", required=True)
    status = fields.Selection([('in_progress', 'In Progress'),
                               ('done', 'Done')
                               ],
                              string="Current Status", required=True)
    remarks = fields.Text(string="Remarks")
    currency_id = fields.Many2one('res.country', string="Currency")
    maintenance_on = fields.Many2one("product.product", string="Maintenance on")
    vendor = fields.Many2one("product.product", string="Vendor")
    cost = fields.Monetary(string="Cost")
    uom_id = fields.Many2one('uom.uom', string="UOM")


class ServiceChargeLines(models.Model):
    _name = 'service.charge.lines'
    _description = "Service Charge Lines"

    product = fields.Many2one('product.product', string="Product")
    currency_id = fields.Many2one('res.country', string="Currency")
    service_cost = fields.Monetary(string="Service Cost")
    service_charge_ids = fields.Many2one("preventive.maintenance", string="Service Charge ID")
