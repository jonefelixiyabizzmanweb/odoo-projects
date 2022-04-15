# -*- coding: utf-8 -*-

{
    "name": "Sales Person Planning",
    'version': '14.0',
    "author": "BizzmanWeb",
    "website": "",
    'images': [],
    'sequence': -1,
    'summary': "Module helps us to plan the daily schedule of a sales person",
    'category': 'Sale',
    "depends": [
        "contacts",'mail','sale',
    ],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "data/templates.xml",
        "wizard/lost.xml",
        "views/sales_planning_configuration.xml",
        "views/sales_planning.xml",
        "views/sales_schedule.xml",
        'views/menu.xml',
    ],
    "qweb": [
        # 'static/src/xml/tree_view_button.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


