from odoo import models, fields

GENDER_LIST = [('male', "MALE"), ('female', "FEMALE"), ('others', "OTHERS")]

# Blood group

class BloodGroup(models.Model):
    _name = "blood.group"
    _description = "Blood Group"
    _rec_name = "blood_name"

    blood_name = fields.Char("Name", required=True)
    code = fields.Char("Code")

#  Bus Type

class Bustype(models.Model):
    _name= "bus.type"
    _description = "Bus Type"
    _rec_name = "bus_type"

    bus_type = fields.Char("Type Name")
    code = fields.Char("Code")

# Bus Model

class BusModel(models.Model):
    _name = "bus.model"
    _description = "Bus Model"
    _rec_name = "model_name"

    model_name = fields.Char("Model Name")
    code = fields.Char("Code")
    make = fields.Char("Make")
    brand = fields.Char("Brand")
    brand_image = fields.Image("Brand Image")

class Booking(models.Model):
    _name = "booking"
    _description = "To Booking"
    _rec_name = "name"

    name = fields.Char("Name")
    gender = fields.Selection(GENDER_LIST,"Gender")
    age = fields.Integer("Age")

class District(models.Model):
    _name = "name.district"
    _description = "To District"
    _rec_name = "district_name"

    district_name = fields.Char("District")
    code = fields.Char("Code")
    state_id = fields.Many2one('res.country.state',"State")

class PickDrop(models.Model):
    _name = "pickup.drop"
    _description = "to Pick up drop information"

    name = fields.Char("Name")
    code = fields.Char("Code")
    district_id = fields.Many2one('name.district',"District")

class Route(models.Model):
    _name = "route.details"
    _description = "to Pick up route  information"
    _rec_name = "route_name"

    route_name = fields.Char("Route Name")
    code = fields.Char("Code")
    from_point = fields.Many2one('name.district',"From")
    to_point = fields.Many2one('name.district',"To")

class Fare(models.Model):
    _name = "fare.details"
    _description = "to Pick up fare information"

    route_name = fields.Many2one('route.details', "Route Name")
    fare = fields.Integer("Fare")



