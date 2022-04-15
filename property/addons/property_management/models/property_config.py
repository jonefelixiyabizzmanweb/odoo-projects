from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class PropertyType(models.Model):
    _name = "property.type"
    _description = "Property Type"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)



class AmcValidity(models.Model):
    _name = "amc.validity"
    _description = "AMC Validity Years"
    _rec_name = "validity"

    validity = fields.Char(string='Validity', required=True)
    amount = fields.Float(string="Amount", required=True)

class RepairingPeriod(models.Model):
    _name = "repairing.period"
    _description = "Repairing Period"
    _rec_name = "period"

    period = fields.Char(string='Period Applicable', required=True)


class BlockDetails(models.Model):
    _name = "block"
    _description = "block"
    _rec_name = "block_name"

    block_name = fields.Char(string="Block Name")
    # code = fields.Char(string="Code")
    # no_of_blocks  = fields.Integer(string="Number of Blocks")
    project = fields.Many2one('project.details',"Project Name")

class LocationDetails(models.Model):
    _name = "location.details"
    _description = "Location Details"
    _rec_name = "location"

    location = fields.Char(string="Location Name")
    street = fields.Char(string="Street1")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    state_id = fields.Many2one('res.country.state', string="State")
    country_id = fields.Many2one('res.country', string="Country")
    zip = fields.Char(string="Zip Code", required=True)

class ProjectDetails(models.Model):
    _name = "project.details"
    _description = "project details"
    _rec_name = "project_name"

    project_name = fields.Char(string="Project Name")
    # code = fields.Char(string="Code")
    # block = fields.Many2one('block',string="Block Name")
    location = fields.Many2one('location.details',string="Location")

class Uom(models.Model):
    _name = "uom"
    _description = "unit of measurement"
    _rec_name = "uom"

    uom = fields.Many2one('uom.uom',string="Unit of Measurement")
    # code = fields.Char(string="Code")

# class list(models.Model):
#     _name = "list"
#     _description = "flats information"
#     _rec_name = "flat_name"
#
#     flat_name = fields.Char(string="Flat name list")

class ReferenceField(models.Model):
    _name = "reference.form"
    
    _rec_name = "name"

    name = fields.Char(string="Reference")
    
    
class SourceField(models.Model):
    _name = "source.form"
    
    _rec_name = "name"

    name = fields.Char(string="Source Name")
    mobile = fields.Char(string="Mobile Number")
    email = fields.Char(string="Email")
    
    
class AmenitiesField(models.Model):
    _name = "amenities.form"
    
    _rec_name = "name"

    name = fields.Char(string="Amenities")
    basis = fields.Char(string="Basis")
    uom = fields.Many2one('uom',string="UoM")