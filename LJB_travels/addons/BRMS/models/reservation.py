from odoo import fields,models,api



class Reservation(models.Model):
    _name="reservation.details"
    _description ="To store reservation details"
    _rec_name="code"

    bus_name = fields.Many2one('bus.details', string="Bus Name")
    bus_type = fields.Many2one('bus.type', string="Bus Type")
    code = fields.Char(string="Reservation Id", default=lambda self: 'new')
    from_point = fields.Many2one('name.district',"From")
    pick_up = fields.Many2one('pickup.drop', "Pick up Point")
    to_point = fields.Many2one('name.district', "To")
    drop_point = fields.Many2one('pickup.drop', "Drop Point")
    schedule_date = fields.Date(string="Date")
    route_name = fields.Many2one('route.details',"Route Name")
    reserved_seat = fields.Integer(string="Reserved Seat",default="10")
    available_seat = fields.Integer(string="Available Seat",default="10")
    selected_seat = fields.Boolean(string="Selected Seat")
    fare = fields.Integer(string="Fare")
    number_of_tickets = fields.Integer(string="Number of tickets")
    total_amount = fields.Integer(string="Total",compute='_compute_total')
    state = fields.Selection([('draft',"Draft"),('done',"Done"),('confirm',"Confirm"),('booking',"Booking"),('cancel',"Cancel")],string="State")

    def action_draft(self):
        print(".....draft")
        self.state = "draft"

    def action_done(self):
        print(".....done")
        self.state = "done"

    def action_confirm(self):
        print(".....confirm")
        self.state = "confirm"

    def action_booking(self):
        print(".....booking")
        self.state = "booking"
    def action_cancel(self):
        print(".....cancel")
        self.state = "cancel"

    @api.depends('fare','number_of_tickets')
    def _compute_total(self):
        self.total_amount = False
        for rec in self:
            if rec.fare * rec.number_of_tickets:
                self.total_amount = rec.fare * rec.number_of_tickets


    @api.model
    def create(self, vals):
        if vals.get('code', ('new')) == ('new'):
            vals['code'] = self.env['ir.sequence'].next_by_code('BRMS.reservation.details') or ('new')
        return super(Reservation, self).create(vals)

    # @api.depends('amount','number_of_tickets')
    # def _compute_total(self):
    #     print("success")
    #     for rec in self:
    #         rec.total_amount = rec.amount*