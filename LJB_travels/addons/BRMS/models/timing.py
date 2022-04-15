from odoo import fields,models,api
from datetime import date


class Timing(models.Model):

    _name="timing.details"
    _description="To store timing details"
    # _inherit =['mail.thread','mail.activity.mixin']
    # _rec_name ="bus_name"


    bus_name = fields.Many2one('bus.details',string="Bus")
    bus_type = fields.Many2one('bus.type',string="Bus Type")
    route_name = fields.Many2one('route.details',string="Route")
    timing = fields.Datetime(string="Timing Details")
