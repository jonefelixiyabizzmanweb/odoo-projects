# -*- coding: utf-8 -*-

{
    "name": "Ketex Customer",
    'version': '14.0',
    "author": "BizzmanWeb",
    "website": "",
    'images': [],
    'sequence': -1,
    'summary': "Module helps us to plan the daily schedule of a sales person",
    'category': 'Sale',
    "depends": [
        "contacts",
    ],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/new_customer.xml",
        "views/config.xml",
    ],
    "qweb": [
        # 'static/src/xml/tree_view_button.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


