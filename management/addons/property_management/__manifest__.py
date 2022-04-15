# -*- coding: utf-8 -*-

{
    "name": "Property Management",
    'version': '14.0',
    "author": "BizzmanWeb",
    "website": "",
    'images': ['static/description/icon.png'],
    'sequence': -1,
    'summary': "Module helps us to check the different kind of property",
    'category': 'Manufacturing',
    "depends": [
        "mail","sale_management","sale","web","crm","project","stock","account"
    ],
    "license": "LGPL-3",
    "data": [
        'security/ir.model.access.csv',
        "data/sequence.xml",
        "views/product_inherit.xml",
        "views/property_details.xml",
        "views/property_details_new.xml",
        "views/property_sale.xml",
        "wizards/renewal.xml",
        "wizards/flat_details_new.xml",
        "wizards/flat_details_tree.xml",
        "wizards/flat_apreview.xml",
        "views/property_maintenance.xml",
        # "views/web_assets.xml",
        "views/property_leads.xml",
        "views/property_config.xml",
        "views/quotation_inherit.xml",
        "views/invoice_inherit.xml",
        # "views/property_product.xml",

    ],
    
    #  "qweb":[
    #     'static/src/xml/widget_view.xml',
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
