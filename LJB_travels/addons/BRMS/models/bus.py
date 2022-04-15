from odoo import fields, models,api


class Bus(models.Model):
    _name = "bus.details"
    _description = "To store bus details"
    _rec_name = "bus_name"

    bus_name = fields.Char(string="Bus Name", required="True")
    bus_type = fields.Many2one('bus.type',string="Bus Type")
    model_name =fields.Many2one('bus.model',string="Bus Model")
    code = fields.Char(string="Code", default=lambda self: 'new' )
    number_plate = fields.Char(string="Number plate")
    seat_capacity = fields.Integer(string="Seat Capacity")
    fuel_capacity = fields.Integer(string="Fuel Capacity")
    odoometer = fields.Char(string="Odoometer")
    organization = fields.Many2one('organization.details',string="Organization")
    image = fields.Image("Bus Image")

    @api.model
    def create(self, vals):
        if vals.get('code', ('new')) == ('new'):
            vals['code'] = self.env['ir.sequence'].next_by_code('BRMS.bus.details') or ('new')
        return super(Bus, self).create(vals)

    @api.model
    def create(self, vals_list):
        print("CREATE FUNCTION")
        print(vals_list)
        vals_list['bus_name'] = vals_list.get('bus_name').upper()
        return super(Bus, self).create(vals_list)
