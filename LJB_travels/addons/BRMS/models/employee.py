from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from _datetime import date
from odoo.osv import expression
import re




GENDER_LIST = [('male', "Male"), ('female', "Female"), ('others', "Others")]
LIST = [('single', "Single"), ('married', "Married")]
DESIGN=[('Driver','Driver'),('conductor','Conductor')]

class Employee(models.Model):
    _name = 'employee.details'
    _description = "To store employee personal information"
    _rec_name = 'employee_name'

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'IN')], limit=1)

        return country

    @api.model
    def _get_default_state(self):
        state = self.env['res.country.state'].search([('name', '=', 'Tamil Nadu'), ('code', '=', 'TN')], limit=1)

        return state

    employee_name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Employee Id",default=lambda self: 'new',  required=True)
    designation = fields.Selection(DESIGN,string="Desigination", required=True)
    father_name = fields.Char(string="Father Name")
    mother_name = fields.Char(string="Mother Name")
    email_id = fields.Char(string="Email Id")
    gender = fields.Selection(GENDER_LIST, string="Gender", default="male")
    dob = fields.Date(string="Date of birth", required=True)
    age = fields.Integer(string="Age", _compute= "_compute_age")
    blood_name_id = fields.Many2one('blood.group',string="Blood Group")
    experience = fields.Integer(string="Experience", required=True)
    language_ids = fields.Many2many('language.details', string="language knows")
    marital_status = fields.Selection(LIST, string="Marital Status")
    mobile= fields.Char(string="Mobile", required=True)
    image = fields.Image(string="Image", max_width=100, max_height=100)
    address1 = fields.Char(string="Address1")
    address2 = fields.Char(string="Address2")
    district_id = fields.Many2one('name.district',string="District")
    state_id = fields.Many2one('res.country.state', string="State",default=_get_default_state)
    country_id = fields.Many2one('res.country', string="Country",default=_get_default_country)
    pin_code = fields.Char(string="Pin code", size=6)
    aadhaar_no = fields.Char(string="Aadhaar No", required=True)
    bus_handling = fields.Many2one('bus.details',string="Bus Handling")
    salary = fields.Integer(string="Salary")


    @api.model
    def create(self, vals):
        if vals.get('code', ('new')) == ('new'):
            vals['code'] = self.env['ir.sequence'].next_by_code('BRMS.employee.details') or ('new')
        return super(Employee, self).create(vals)

    @api.model
    def create(self, vals_list):
        print("CREATE FUNCTION")
        print(vals_list)
        vals_list['employee_name'] = vals_list.get('employee_name').upper()
        return super(Employee, self).create(vals_list)

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        if self.dob:
            self.age = fields.Date.today().year - self.dob.year

    @api.constrains('dob')
    def check_age(self):
        '''Method to check age should be greater than 18'''
        current_dt = fields.Date.today()
        if self.dob:
            start = self.dob
            age_calc = ((current_dt - start).days / 365)
            # Check if age less than 18 years
            if age_calc < 18:
                raise ValidationError('Age of employee should be greater than 18 years!')

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
