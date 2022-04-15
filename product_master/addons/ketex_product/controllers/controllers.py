# -*- coding: utf-8 -*-
# from odoo import http


# class KetexProduct(http.Controller):
#     @http.route('/ketex_product/ketex_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ketex_product/ketex_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ketex_product.listing', {
#             'root': '/ketex_product/ketex_product',
#             'objects': http.request.env['ketex_product.ketex_product'].search([]),
#         })

#     @http.route('/ketex_product/ketex_product/objects/<model("ketex_product.ketex_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ketex_product.object', {
#             'object': obj
#         })
