from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr
import datetime

import math
import base64

class PropertyDetails(models.Model):
    _name='property.product'
    _description = 'Property Details'
    _rec_name='project_id'
    
    project_id = fields.Many2one('project.details',string="Project")
    sale_ok = fields.Boolean('Can be Sold', default=True)
    # purchase_ok = fields.Boolean('Can be Purchased', default=True)
    block_id = fields.Many2one('block',string="Block Name",domain="[ ('project', '=', project_id)]")
    location = fields.Many2one(string="Location", related="project_id.location")
    no_flats = fields.Integer(string="No.of.Flats")
    # flat = fields.Integer(string="Flat")
    # flat_name = fields.Char(string='Flat Name/No')
    # area = fields.Float(string="Area(SB) Sq.ft")
    # bhk = fields.Char(string="BHK")
    # level = fields.Char(string="Level")
    # rate_per_sq = fields.Float(string="Rate/Sq.ft")
    # total_amount = fields.Float(string="Total(Rs)",compute='compute_rate')
    flat_ids = fields.One2many('flat', 'flat_line_ids', string="")
    building_block = fields.Many2one('block', string="Block Name")
    flat_name = fields.Char(string='Flat Name/No')
    area = fields.Float(string="Qty")
    bhk = fields.Char(string="BHK")
    level = fields.Char(string="Level")
    rate_per_sq = fields.Float(string="Rate")
    total_amount = fields.Float(string="Total(Rs)",compute='compute_rate')
    flat_line_ids = fields.Many2one('property.product',string="Flate Line Id")
    status = fields.Selection([('1','Available'),('2','Sold')],string="Status",default="1")
    
    
    @api.depends('area', 'rate_per_sq')
    def compute_rate(self):
        for line in self:
            line.total_amount= line.area * line.rate_per_sq
            
    @api.onchange('block_id')
    def _onchange_state_pro(self):
        # self.flat_ids = self.env['block'].search([('building_block','=',self.block_id)])
        for rec in self:
            lines = []
            for line in self.block_id:
                val = {
                    # 'project': self.project.id ,
                    'building_block': self.block_id.id,
                    # 'flat_no': self.flat_product.id
                    }
                lines.append((0,0,val))
            rec.flat_ids = lines

            
            
    # @api.onchage('flat_ids')
    # def _onchange_block(self):
        # for rec in self:
            # line=[]
            # for line in self.flat_ids:
                # val = {
                    # 'building_block':self.block_id.id,
                    # }
                # lines.append((0,0,val))
            # rec.flat_ids = lines
            
            
    # def flat(self):
        # for line in self:
            # return line
    # def default_get(self,cr,uid,ids,context=None):
        # res={}
        # if context:
            # context_keys = context.keys()
            # next_sequence = self.block_id
            # if 'flat_ids' in context_keys:
                # if len(context.get('flat_ids'))>0:
                    # next_sequence= self.block_id
        # res.update({'building_block':next_sequence})
        # return res
        
        
    # @api.one
    # def flat(self):
        # self.ensure_one()
        # for record in self:
                # i=[]
                # # vals = self.env.ref('flat').search[('building_block','=', self.building_block)]
                # vals = self.env['flat'].search([('building_block','=', self.block_id.id)])
                # for j in vals:
                    # i.append(0,0,{
                        # 'building_block': vals.building_block.id,
                        # 'flat_name': vals.flat_name,
                        # 'area': vals.area,
                        # 'bhk': vals.bhk,
                        # 'status': vals.status,
                        # 'rate_per_sq': vals.rate_per_sq,
                        # 'level': vals.level,
                        # 'total_amount': vals.total_amount
                        # })
                    
        # view_id = self.env.ref('property_management.flat_details_wizard_view')
        # return {
            # 'type': 'ir.actions.act_window',
            # 'res_model': 'flat.details',
            # 'view_type': 'tree',
            # 'view_mode': 'form',
            # 'target': 'new',
            # # 'res_id': j.id,
            # 'view_id': view_id.id,
            # 'views': [(view_id.id, 'form')],
            # 'context': {'default_flat_ids': i,
            # }
        # }
        
        
    # @api.multi
    def flat(self):
        self.ensure_one()
        flatdetails = [(4, flat.id, 0) for flat in self.flat_ids]
        view_id = self.env.ref('property_management.flat_details_wizard_view')
        result = {
            'type': 'ir.actions.act_window',
            'res_model': 'flat.details',
            'view_type': 'tree',
            'view_mode': 'form',
            'target': 'new',
            # 'res_id': j.id,
            'view_id': view_id.id,
            'views': [(view_id.id, 'form')],
            'context': {'default_flat_ids': flatdetails}

        }
        return result
        # do = self.env[('building_block','=',self.block_id)]
        # return{
            # 'name'          :   ('Project Cashflow Report'),
            # 'type'          :   'ir.actions.act_window',
            # 'view_type'     :   'form',
            # 'view_mode'     :   'tree',
            # 'target'        :   'new', 
            # 'res_model'     :   'flat',
            # 'view_id'       :   False,
            
            # }    
        
    # @api.multi
    # def flat(self,context=None):
    # field_ids = self.env['property.product'].search([]).ids
    
    # domain = [('id','in',field_ids)]

    # view_id_tree = self.env['ir.ui.view'].search([('name','=',"model.tree")])
    # return {
        # 'type': 'ir.actions.act_window',
        # 'res_model': 'flat',
        # 'view_type': 'form',
        # 'view_mode': 'tree,form',
        # 'views': [(view_id_tree[0].id, 'tree'),(False,'form')],
        # 'view_id ref="module_name.tree_view"': '',
        # 'target': 'current',
        # 'domain': domain,
    # }
      
         # parameter_lines = []
        # prd_reference_id = self.env['property.product'].search([])
        # print('---------------------------Prd Reference No.----------------', prd_reference_id)

        # for i in self.block_id:
            # print('---------------------------Prd Reference No.----------------', i.id, i.name)
            # l = self.env['flat'].search([])
            # for j in prd_reference_id:
                # print('---------------------------Prd Reference Val.----------------', j.id, j.name)
                # if i.id == j.id:
                    # prd_reference_val = self.env['flat'].browse([(j.id)])
                    # # print('---------------------------Done----------------', j.name, j.default_code)

                    # for k in j.flat_ids:
                                # print('---------------------------Prd Reference Val.----------------', k.name_serial)

                        # parameter_vals = (0, 0, {
                            # 'building': k.building_block,
                            # 'flat_name': k.flat_name,
                            # 'area': k.area,
                            # 'bhk': k.bhk,
                            # 'status': k.status,
                            # 'rate_per_sq': k.rate_per_sq,
                            # 'level': k.level,
                            # 'total_amount': k.total_amount
                        # })

                        # print('---------------------------Vals.----------------', parameter_vals)

                        # form_reference_val.write(parameter_vals)
                        # parameter_lines.append(parameter_vals)
            
            
class Flat(models.Model):
    _name = "flat"
    _description = "flat basic Details"
    _rec_name = "flat_name"

    building_block = fields.Many2one('block', string="Block Name")
    flat_name = fields.Char(string='Flat Name/Shop',domain=[("status", '=', '1')])
    area = fields.Float(string="Qty")
    bhk = fields.Char(string="BHK")
    level = fields.Char(string="Level")
    rate_per_sq = fields.Float(string="Rate")
    total_amount = fields.Float(string="Total(Rs)",compute='compute_rate')
    flat_line_ids = fields.Many2one('property.product',string="Flate Line Id")
    status = fields.Selection([('1','Available'),('2','Sold'),('3','On Hold'),('4','On Progress')],string="Status",default="1")
    c_date = fields.Date("Dead Line")
    # amenities = fields.Many2one('amenities.form',string="Amenities")
    product_uom = fields.Many2one('uom.uom',string="UoM")
    
    @api.depends('area', 'rate_per_sq')
    def compute_rate(self):
        for line in self:
            line.total_amount= line.area * line.rate_per_sq
            
          
    def reverse_state(self):
         
        for rec in self.search([('status', '=', '3')]):
            if rec.c_date and rec.c_date <= fields.Date.today():
                rec.write({'status': '1'})      
            
            
    # def update_status(self):
        # test = self.pool.get('sale.order').search([('building_block','=','self.building_block'),('flat_product','=','self.flat_name')])
        # if test:
            # return self.write({"status": "2"})
            
            
    # @api.onchange('flat_name')
    # def onchange_flat_name(self):
        # variant_ids_list = []
        # if self._context.get('block_id'):
            # block_id1 = self.env["block"].browse(self._context.get('block_id'))
            # for block_id in block_id1.block_id:
                 
        
        
            
        