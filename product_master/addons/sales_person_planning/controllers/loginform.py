from odoo import http
from odoo.http import request


@http.route('/add_login', auth='user', type='http', website=True)
def add_login(self, **k):
    user_name = k['c_name']
    password = k['password']


    request.env['sales.planning'].create({
        'c_name': user_name,
        'password': password,

    })
    return request.render("sales_person_planning.login_success", {})



