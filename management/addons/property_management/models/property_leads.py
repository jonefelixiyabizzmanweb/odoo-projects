from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero
from odoo.tools import float_compare, float_round, float_repr

import math
import base64


class CRMInherit(models.Model):
    _inherit = 'crm.lead'
    _rec_name = 'lead_enquiry'
  
    # name = fields.Char(required=False)
    # enquiry_form = fields.Many2one('res.users',"Enquiry Form",required=True)
    # agent_name = fields.Many2one('res.users',"Agent Name")
    # lead_name = fields.Many2one('res.users',"Lead Name")
    # lead_enquiry = fields.Text(string="Lead Enquiry")
    # state_pro = fields.Selection([('1','Accept'),('2','Reject')],string="Status",default='1')
    # project = fields.Many2one('res.users',"Project")
    # building_block = fields.Many2one('res.users',"Building Block")
    # flat_product = fields.Many2one('res.users',"Flat/Product")
    # qty = fields.Many2one('res.users',"Qty")
    # reference = fields.Many2one('res.users',"Reference")
    
    
    name = fields.Char(required=False)
    enquiry_form = fields.Selection([('1','Realtors'),('2','Media'),('3','Referal'),('4','Director'),('5','Employee')],string="Enquiry From",default='1')
    source_name = fields.Many2one('source.form',"Source Name")
    # lead_name = fields.Many2one('res.partner',"Lead Name")
    lead_enquiry = fields.Text(string="Lead Enquiry")
    state_pro = fields.Selection([('1','Interested'),('2','Not Interested'),('3','On Hold')],string="Status")
    project = fields.Many2one('project.details',"Project")
    building_block = fields.Many2one('block',"Building Block",domain="[ ('project', '=', project)]")
    flat_product = fields.Many2one('flat',"Flat/Product",domain="[('building_block', '=', building_block)]")
    rate_per_sq = fields.Float(string="Rate",related='flat_product.rate_per_sq')
    reference = fields.Many2one('reference.form',"Reference")
    email_from = fields.Char(related="partner_id.email",string="Lead Email")
    phone = fields.Char(related="partner_id.mobile",string="Lead mobile")
    bhk = fields.Char(related='flat_product.bhk',string="BHK")
    area_sq = fields.Float(string="Qty",related='flat_product.area')
    location = fields.Many2one(string="Location",related="project.location")
    partner_id = fields.Many2one(
        'res.partner', string='Customer', index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    lead_approval = fields.Selection([('1','Yes'),('2','No')],string="Lead Approval")
    types = fields.Selection([('1','Commercial'),('2','Residential')],string="Type")
    # amenities = fields.Many2one(related='flat_product.amenities',string="Amenities")
    product_uom = fields.Many2one(related='flat_product.product_uom',string="UoM")
        
    # def action_new_quotation(self):
        # result = super(CRMInherit, self).action_new_quotation()
        # action = self.env["ir.actions.actions"]._for_xml_id("sale_crm.sale_action_quotations_new")
        # action['context'] = {
            # 'search_default_opportunity_id': self.id,
            # 'default_opportunity_id': self.id,
            # 'search_default_partner_id': self.partner_id.id,
            # 'default_partner_id': self.partner_id.id,
            # 'default_campaign_id': self.campaign_id.id,
            # 'default_medium_id': self.medium_id.id,
            # 'default_origin': self.name,
            # 'default_source_id': self.source_id.id,
            # 'default_company_id': self.company_id.id or self.env.company.id,
            # 'default_tag_ids': [(6, 0, self.tag_ids.ids)],
            # 'default_agent': self.agent_name.id
         # }
        # if self.state_pro:
            # action['context']['default_state_pro'] = self.state_pro.id,
        # if self.user_id:
            # action['context']['default_user_id'] = self.user_id.id
        # return ['action','result']
        
    # def action_sale_quotations_new(self):
        # if not self.partner_id:
            # return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
        # else:
            # return self.action_new_quotation()

    # def action_new_quotation(self):
        # action = self.env["ir.actions.actions"]._for_xml_id("sale_crm.sale_action_quotations_new")
        # action['context'] = {
            # 'search_default_opportunity_id': self.id,
            # 'default_opportunity_id': self.id,
            # 'search_default_partner_id': self.partner_id.id,
            # 'default_partner_id': self.partner_id.id,
            # 'default_campaign_id': self.campaign_id.id,
            # 'default_medium_id': self.medium_id.id,
            # 'default_origin': self.name,
            # 'default_source_id': self.source_id.id,
            # 'default_company_id': self.company_id.id or self.env.company.id,
            # 'default_tag_ids': [(6, 0, self.tag_ids.ids)],
            # 'default_agent': self.agent_name.id
         # }
        # if self.state_pro:
            # action['context']['default_state_pro'] = self.state_pro.id,
        # if self.user_id:
            # action['context']['default_user_id'] = self.user_id.id
        # return action
        
        
        
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    state_pro = fields.Selection([('1','Interested'),('2','Not Interested'),('3','On Hold')],string="Status")
    # ,related='opportunity_id.state_pro')
    # ,related='opportunity_id.state_pro'
    source_name = fields.Many2one('source.form',"Source Name")
    # ,related='opportunity_id.source_name'
    project = fields.Many2one('project.details',"Project")
    # ,related='opportunity_id.project'
    building_block = fields.Many2one('block',"Building Block",domain="['|', ('project', '=', False), ('project', '=', project)]")
    # ,related='opportunity_id.building_block'
    flat_product = fields.Many2one('flat',"Flat/Product",domain="['|',('building_block', '=', building_block),('building_block', '=', False)]")
    # ,related='opportunity_id.flat_product'
    # qty = fields.Many2one('res.users',"Qty")
    reference = fields.Many2one('reference.form',"Reference")
    # ,related='opportunity_id.reference'
    bhk = fields.Char(related='flat_product.bhk',string="BHK")
    area_sq = fields.Float(string="Qty",related='flat_product.area')
    location = fields.Many2one(string="Location",related="project.location")
    rate_per_sq = fields.Float(string="Rate",related='flat_product.rate_per_sq')
    # amenities = fields.Many2one(related='flat_product.amenities',string="Amenities")
    product_uom = fields.Many2one(related='flat_product.product_uom',string="UoM")
    status = fields.Selection([('1','Occupied'),('2','Sold')],string="Availability",default="1")
    
    # def _prepare_invoice(self):
        # invoice_vals = super(SaleOrderInherit, self)._prepare_invoice()
        # # invoice_vals['project'] = self.project.id  or False
        # invoice_vals['invoice_line_ids'] = [(1, product_id.id, {'project': line.project})for line in self.order_line]
        # return invoice_vals
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrderInherit, self)._prepare_invoice()
        invoice_vals['project'] = self.project.id  or False
        invoice_vals['flat_no'] = self.flat_product.id  or False
        invoice_vals['block'] = self.building_block.id  or False
        invoice_vals['bhk'] = self.bhk  or False
        # invoice_vals['types'] = self.types  or False
        invoice_vals['location'] = self.location.id  or False
        return invoice_vals
    # def _prepare_invoice_line(self):
        # res = super(SaleOrderInherit, self)._prepare_invoice_line()
        # res.update({'flat_no': self.flat_no, })
        # return res 
        
    @api.onchange('project')
    def _onchange_state_pro(self):
        for rec in self:
            lines = []
            for line in self.project:
                val = {
                    'project': self.project.id ,
                    'block': self.building_block.id,
                    'flat_no': self.flat_product.id,
                    'bhk':self.bhk,
                    'price_unit':self.rate_per_sq,
                    'product_uom_qty':self.area_sq,
                    'location':self.location.id,
                    # 'amenities':self.amenities.id,
                    # 'product_id': 'property',
                    'uom':self.product_uom.id,
                    }
                lines.append((0,0,val))
            rec.order_line = lines
            
    # @api.onchange('state')
    # def _onchange_state(self):
        # if self.state=='sale':
            # return self.write({"status": "2"})
            # flats = self.env['flat'].search([('flat_name','=',self.flat_product.id)])
            # for rec in flats:
                # self.env.cr.execute("update flat set status=2")
                # self.env.cr.commit()
            # # print(rec)
            # s = flats.update({'status':'2'})
            # return s
            
                
    
    
    # def action_confirm(self):
        # self.ensure_one()
        # flatdetails = [(4, flat.id, 0) for flat in self.flat_ids]
        # view_id = self.env.ref('property_management.flat_details_wizard_view')
        # result = {
            # 'type': 'ir.actions.act_window',
            # 'res_model': 'flat.details',
            # 'view_type': 'tree',
            # 'view_mode': 'form',
            # 'target': 'new',
            # # 'res_id': j.id,
            # 'view_id': view_id.id,
            # 'views': [(view_id.id, 'form')],
            # 'context': {'default_flat_ids': flatdetails}

        # }
        # return result
    def action_confirm(self):
        result = super(SaleOrderInherit, self).action_confirm()
        self.write({"status": "2"})
        # for rec in self:
            # flats = self.env.ref('flat').search(['flat_name','=',self.flat_product.id])
            # for i in flats:
                # i.update({'status':'2'})
        return result
        # for rec in self:
        # flats = self.env['property.product'].search([('project_id','=',self.project.id)])
            # for record in flats:
                # record.update((1,flat_ids,{'flat_ids.status':'2'}))
                # return record
        # flats = self.env['flat'].search([('flat_name','=',self.flat_product.id)])
        # if flats:
            # s = flats.({'status':'2'})
            # return s 
        # for rec in flats:
            # rec = { 'status':'2'
            # }
            # self.env['property.product'].update(rec) 
            # return
        # for rec in self:
            # flats = self.env.ref('property_management.flat_details_wizard_view').browse([('flat_name','=',self.flat_product)])
            # if flats:
        # self.env.cr.execute("update flat set status=2 where flat_name = %s",[self.flat_product])
        # self.env.cr.commit()
    
    
    
    
    
    # def action_sale_quotations_new(self):
        # vals = {'partner_id':self.partner_id.id
        # }
        # self.env['sale.order'].create(vals)












    # @api.onchange('project')
    # def onchange_project(self):
        # b={}
        # if self.project:
            # c = self.env['product.template']._search([('self.project''=''name')])

    # @api.constrains('partner_id', 'state_pro')
    # def check_partner_id(self):
    #     for record in self:
    #         obj = self.search([('partner_id', '=', record.partner_id), (record.state_pro, '!=', "2")])
    #         if obj:
    #             raise Warning("warning", "already")
    
    # def action_sale_quotations_new(self):
        # result = super(CRMInherit, self).action_sale_quotations_new()
        # if not self.partner_id:
            # return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
        # else:
            # return [result, self.action_new_quotation_inherit()]
        
        
    # def action_new_quotation_inherit(self):
        # action = self.env["ir.actions.actions"]._for_xml_id("sale_crm.sale_action_quotations_new")
        # action['context'] = {
            
            # 'default_agent': self.agent_name.id,
            # 'search_default_partner_id': self.partner_id.id,
            # 'default_partner_id': self.partner_id.id,
            # 'default_campaign_id': self.campaign_id.id,
            # 'default_medium_id': self.medium_id.id,
            # 'default_origin': self.name,
            # 'default_source_id': self.source_id.id,
            # 'default_company_id': self.company_id.id or self.env.company.id,
            # 'default_tag_ids': [(6, 0, self.tag_ids.ids)]
         # }
        # return action