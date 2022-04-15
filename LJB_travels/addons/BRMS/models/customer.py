from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from _datetime import date
from odoo.osv import expression
import re

GENDER_LIST = [('male', "MALE"), ('female', "FEMALE"), ('others', "OTHERS")]

class Customer(models.Model):
    _name = 'customer.details'
    _description = "To store customer personal information"

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'IN')], limit=1)
        return country

    @api.model
    def _get_default_state(self):
        state = self.env['res.country.state'].search([('name', '=', 'Tamil Nadu'), ('code', '=', 'TN')], limit=1)
        return state

    name = fields.Char(string="Name", required=True)
    email_id = fields.Char(string="Email Id")
    code = fields.Char("Customer ID" , default=lambda self: 'new')
    gender = fields.Selection(GENDER_LIST, string="Gender")
    mobile = fields.Char(string="MOBILE")
    dob = fields.Date(string="Date of birth")
    father_name = fields.Char(string="Father name")
    language_ids = fields.Many2many('language.details', string="language Knows")
    age = fields.Integer(string="Age" , _compute= "_compute_age")
    blood_name_id = fields.Many2one('blood.group',string="Blood Group")
    aadhar_no = fields.Char(string="Aadhar No")
    address1 = fields.Char(string="Address 1")
    address2 = fields.Char(string="Address 2")
    district_id = fields.Many2one('name.district',string="District")
    state_id = fields.Many2one('res.country.state', string="State",default=_get_default_state)
    country_id = fields.Many2one('res.country', string="Country",default=_get_default_country)
    pin_code = fields.Char(string="Pin code" ,size=6)

    @api.model
    def create(self, vals):
        if vals.get('code', ('new')) == ('new'):
            vals['code'] = self.env['ir.sequence'].next_by_code('BRMS.customer.details') or ('new')
        return super(Customer, self).create(vals)

    @api.model
    def create(self, vals_list):
        print("CREATE FUNCTION")
        print(vals_list)
        vals_list['name'] = vals_list.get('name').upper()
        return super(Customer, self).create(vals_list)

    @api.depends('dob', 'age')
    def _compute_age(self):
        self.age = 0
        for rec in self:
            if rec.dob:
                print(self.dob.year)
                cur_year = date.today().year
                self.age = cur_year - rec.dob.year


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
