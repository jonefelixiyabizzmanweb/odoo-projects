from odoo import fields,models


class language(models.Model):
    _name = 'language.details'
    _description = "To store the language details"

    name = fields.Char(string="language")
    code = fields.Char(string="code")