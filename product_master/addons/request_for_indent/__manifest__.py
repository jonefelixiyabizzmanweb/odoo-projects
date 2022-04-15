# -*- coding: utf-8 -*-

{
    "name": "Request For Indent",
    'version': '14.0',
    "author": "BizzmanWeb",
    "website": "",
    'images': ['static/description/in and out.png'],
    'sequence': -1,
    'summary': "Module helps us to check product indent",
    'category': 'Manufacturing',
    "depends": [
        "purchase",
        "stock",
        "mrp",
    ],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/request_indent.xml",
        "views/config.xml",
        "views/inherit_indent.xml",

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
