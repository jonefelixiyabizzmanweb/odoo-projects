from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from _datetime import date
from odoo.osv import expression
import re


class Organization(models.Model):
    _name = "organization.details"
    _description = "To store organization details"
    _rec_name = "organization_name"

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'IN')], limit=1)
        return country

    @api.model
    def _get_default_state(self):
        state = self.env['res.country.state'].search([('name', '=', 'Tamil Nadu'), ('code', '=', 'TN')], limit=1)
        return state

    organization_name = fields.Char(string="Organization Name")
    org_code = fields.Char(string="Code", default=lambda self : 'new')
    year_of_start = fields.Date(string="Year of Start")
    approval_license = fields.Image(string="Approval License")
    email_id = fields.Char(string="Email Id")
    total_bus = fields.Char(string="Total Bus")
    total_employees = fields.Char(string="Total Employees")
    contact = fields.Char(string="Contact")
    address1 = fields.Text(string="Address 1")
    district_id = fields.Many2one('name.district',string="District")
    state_id = fields.Many2one('res.country.state', string="State",default=_get_default_state)
    country_id = fields.Many2one('res.country', string="Country",default=_get_default_country)
    pin_code = fields.Char(string="Pin code",size=6)
    website = fields.Char(string="Website")

    @api.model
    def create(self, vals):
        if vals.get('org_code', ('new')) == ('new'):
            vals['org_code'] = self.env['ir.sequence'].next_by_code('BRMS.organization.details') or ('new')
        return super(Organization, self).create(vals)

    @api.model
    def create(self, vals_list):
        print("CREATE FUNCTION")
        print(vals_list)
        vals_list['organization_name'] = vals_list.get('organization_name').upper()
        return super(Organization, self).create(vals_list)

    @api.constrains('email_id')
    def _validate_email_id(self):
        print("Called")
        if self.email_id and re.match(r"\w+@\w+.\w+", self.email_id) == None:
            raise ValidationError("Sorry! invalid mail_id.")

    @api.constrains('mobile')
    def validate_data(self):
        if self.mobile:
            if self.mobile.isalpha() == True:
                raise ValidationError('Kindly Enter the valid phone number')
            if not len(self.mobile) == 10:
                raise ValidationError('Number should have a 10 digits')

