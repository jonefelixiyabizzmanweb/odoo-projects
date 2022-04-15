from odoo import http
from odoo.http import request


class Timing(http.Controller):

    @http.route('/timing', auth='user', type='http',website="True")
    def view_timing(self):
        print("HI")
        timing = []
        timing_ids = request.env['timing.details'].search([])
        for tim in timing_ids:
            timing.append(
                {'bus_name':tim.bus_name,
                 'route_name':tim.route_name,
                 'timing':tim.timing,}
            )
        return request.render('BRMS.timing_details',{'timing':timing})

    @http.route('/customer', auth='user', type='http', website="True")
    def customer(self):


        return request.render('BRMS.customer',{})
