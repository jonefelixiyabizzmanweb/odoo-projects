from odoo import fields,models,api


PAYMENT_LIST = [('online', "ONLINE"), ('cash', "CASH")]
INSURANCE = [('yes',"YES"),('no',"NO")]

class Payment(models.Model):

    _name="payment.details"
    _description="To store payment details"



    payment_id = fields.Char("Payment Id", default=lambda self: 'new')
    reservation_id = fields.Many2one('reservation.details',string="Reservation Id")
    fare = fields.Integer(string="Fare")
    number_of_tickets = fields.Integer(string="No of tickets")
    travel_insurance = fields.Selection(INSURANCE,string="Travel Insurance")
    total_amount = fields.Integer(string="Total Amount")
    payment_type = fields.Selection(PAYMENT_LIST, string="Payment Type")
    grand_total = fields.Integer(string="Grand_total",compute='_compute_grand_total')

    state = fields.Selection(
        [('pay', "Pay"), ('cancel', "Cancel")],
        string="State")

    def action_pay(self):
        print(".....pay")
        self.state = "pay"

    def action_cancel(self):
        print(".....cancel")
        self.state = "cancel"

    @api.model
    def create(self, vals):
        if vals.get('payment_id', ('new')) == ('new'):
            vals['payment_id'] = self.env['ir.sequence'].next_by_code('BRMS.payment.details') or ('new')
        return super(Payment, self).create(vals)

    @api.onchange("reservation_id")
    def update_reservation_id(self):
        print("called")
        for rec in self:
            if rec.reservation_id:
                self.number_of_tickets = rec.reservation_id.number_of_tickets
                self.fare = rec.reservation_id.fare
                self.total_amount = rec.reservation_id.total_amount

    @api.depends('travel_insurance','total_amount')
    def _compute_grand_total(self):
        print("success")
        self.grand_total = False
        for rec in self:
            if rec.travel_insurance =='yes' :
                self.grand_total = 10 + rec.total_amount
            elif rec.travel_insurance == 'no':
                self.grand_total = rec.total_amount