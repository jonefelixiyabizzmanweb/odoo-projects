from odoo import http
from odoo.http import request


class Sales(http.Controller):
    # # planning
    @http.route('/create_planning', type='json', auth='user')
    def create_planning(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'description': rec['name'],
                    'conveyance': rec['conveyance'],

                }
                new_planning = request.env['sales.planning'].sudo().create(vals)
                print("New Planning Is", new_planning)
                args = {'success': True, 'message': 'Success'}
        return args

    @http.route('/get_sales_planning', type='json', auth="none")
    def get_sales_planning(self):
        planning_rec = request.env['sales.planning'].search([])
        planning = []
        for rec in planning_rec:
            vals = {
                'employee_id': rec.employee_id,
                'role_id': rec.role_id,
                'location_id': rec.location_id,
                'start_datetime': rec.start_datetime,
                'end_datetime': rec.end_datetime,
                'tag_ids': rec.tag_ids,
                'allocated_hours': rec.allocated_hours,
                'description': rec.description,
            }
            planning.append(vals)
        data = {'status': 200, 'response': planning, 'message': 'Success'}
        return data

    @http.route('/delete_planning', type='json', auth="none")
    def delete_planning(self):
        if request.jsonrequest:
            for rec in self:
                rec.description.unlink()


    # @http.route('/update_planning', type='json', auth='user')
    # def update_planning(self, **rec):
    #     if request.jsonrequest:
    #         if rec['employee_id']:
    #             print("rec...", rec)
    #             planning = request.env['sales.planning'].sudo().search([('employee_id', '=', rec['employee_id'])])
    #             if planning:
    #                 planning.sudo().write(rec)
    #             args = {'success': True, 'message': 'Planning Updated'}
    #     return args

    @http.route('/create_employee', type='json', auth='user')
    def create_employee(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'description': rec['name'],
                    'allocated_hours': rec['allocated_hours'],



                }
                new_employee = request.env['by.employee'].sudo().create(vals)
                print("New Employee Is", new_employee)
                args = {'success': True, 'message': 'Success'}
        return args

    @http.route('/get_employee', type='json', auth="none")
    def get_employee(self):
        employee_rec = request.env['by.employee'].search([])
        employee = []
        for rec in employee_rec:
            vals = {
                'employee_id': rec.employee_id,
                'role_id': rec.role_id,
                'location_id': rec.location_id,
                'description': rec.description,
                'conveyance ': rec.conveyance,
            }
            employee.append(vals)
        data = {'status': 200, 'response': employee, 'message': 'Success'}
        return data

    # @http.route('/delete_employee', type='json', auth="none")
    # def delete_employee(self):
    #     if request.jsonrequest:
    #         for rec in self:
    #             rec.employee_id.unlink()


    # by role
    @http.route('/create_role', type='json', auth='user')
    def create_role(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'description': rec['name'],
                    'conveyance': rec['conveyance'],

                }
                new_role = request.env['by.role'].sudo().create(vals)
                print("New Role Is", new_role)
                args = {'success': True, 'message': 'Success'}
        return args


    @http.route('/get_role', type='json', auth="none")
    def get_role(self):
        role_rec = request.env['by.role'].search([])
        role = []
        for rec in role_rec:
            vals = {
                'employee_id': rec.employee_id,
                'role_id': rec.role_id,
                'location_id': rec.location_id,
                'description': rec.description,
                'conveyance ': rec.conveyance,

            }
            role.append(vals)
        data = {'status': 200, 'response': role, 'message': 'Success'}
        return data

    #
    # @http.route('/delete_role', type='json', auth="none")
    # def unlink(self,values):
    #     if request.jsonrequest:
    #         for rec in self:
    #             rec.employee_id.unlink()
    #
