# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ketex_config1(models.Model):
    _name = 'ketex.config1'
    _rec_name = 'field1'
    
    
    field1 = fields.Char(string="Field #1")
    code = fields.Char(string="Abbreviation")
    
    
class ketex_config2(models.Model):
    _name = 'ketex.config2'
    _rec_name = 'field2'
    
    # field1 = fields.Many2one('ketex.config1',string="field #1
    field2 = fields.Char(string="Field #2")   
    code = fields.Char(string="Abbreviation")
    field1 = fields.Many2one('ketex.config1',"Field 1")
    
class ketex_config3(models.Model):
    _name = 'ketex.config3'
    _rec_name = 'field3'
    
    field3 = fields.Char(string="Field #3 ")   
    code = fields.Char(string="Abbreviation")
    field2 = fields.Many2one('ketex.config2',"Field 2")
    
    
    
   
class ketex_config4(models.Model):
    _name = 'ketex.config4'
    _rec_name = 'variety'
    
    variety = fields.Char(string="Variety")
    code = fields.Char(string="Abbreviation")
    
    
    
class ketex_config5(models.Model):
    _name = 'ketex.config5'
    _rec_name = 'type_field'
    
    type_field = fields.Char(string="Type")
    code = fields.Char(string="Abbreviation")
    
    
class ketex_config6(models.Model):
    _name = 'ketex.config6'
    _rec_name = 'edge_wall'
    
    edge_wall = fields.Char(string="Edge Wall")
    code = fields.Char(string="Abbreviation")
    


    
class ketex_config8(models.Model):
    _name = 'ketex.config8'
    _rec_name = 'absent'
    
    absent = fields.Char(string="9/10")
    code = fields.Char(string="Abbreviation")
    
    
class ketex_config9(models.Model):
    _name = 'ketex.config9'
    _rec_name = 'c_name'
    
    c_name = fields.Char('Combination Name')
    field1 = fields.Many2one('ketex.config1',string="Field #1")
    bool1 = fields.Boolean("Field 2 ")
    bool0 = fields.Boolean("Field 1 ")
    abb1 = fields.Char('ketex.config1',related="field1.code")
    field2 = fields.Many2one('ketex.config2',string="Field #2")
    bool2 = fields.Boolean("Field 3")
    abb2 = fields.Char('ketex.config2',related="field2.code")
    field3 = fields.Many2one('ketex.config3',string="Field #3")
    # bool3 = fields.Boolean("Field 1 ")
    bool3 = fields.Boolean("Variety")
    abb1 = fields.Char('ketex.config1',related="field1.code")
    abb2 = fields.Char('ketex.config2',related="field2.code")
    abb3 = fields.Char('ketex.config3',related="field3.code")
    gauntlet_variety = fields.Many2one('ketex.config4',string="Variety")
    abb4 = fields.Char('ketex.config4',related="gauntlet_variety.code")
    bool4 = fields.Boolean("Type")
    laterial_type = fields.Many2one('ketex.config5',string="Type")
    bool5 = fields.Boolean("Edge wall")
    edge_wall = fields.Many2one('ketex.config6',string="Edge Wall")
    dia = fields.Float("Dia(mm)")
    panel = fields.Integer("Panel")
    height = fields.Float("Height(mm)")
    tubes = fields.Integer("Tubes")
    pitch = fields.Float("Pitch")
    bool6 = fields.Boolean("Dia")
    bool7 = fields.Boolean("Panel")
    bool8 = fields.Boolean("Height")
    bool9 = fields.Boolean("Tubes")
    bool10 = fields.Boolean("Pitch")
    bool11 = fields.Boolean("9/10")
    absent = fields.Many2one('ketex.config8',"9/10")