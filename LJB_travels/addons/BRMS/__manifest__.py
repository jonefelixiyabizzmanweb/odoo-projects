{
    'name': 'LJB_Travels',
    'version': '1.1',
    'category': 'LJB_Travels/BRMS',
    'sequence': 1,
    'summary': 'To maintain the LJB_Travels information',
    'description': "LJB_Travels Software",
    'website': '',
    'images': [
    ],
    'depends': ['website'


    ],
    'data': [
        'security/ir.model.access.csv',
        'data/config_data.xml',
        'data/sequence.xml',
        'data/templates.xml',
        'wizard/static_wizard.xml',
        'views/reports/static_report.xml',
        'wizard/amount_wizard.xml',
        'views/reports/amount_report.xml',
        'wizard/seat_wizard.xml',
        'views/reports/seat_report.xml',
        'wizard/create_amount.xml',
        # 'views/reports/report_views.xml',
        'views/bus.xml',
        'views/employee.xml',
        'views/customer.xml',
        'views/organization.xml',
        'views/payment.xml',
        'views/reservation.xml',
        'views/res_config.xml',
        'views/language.xml',
        'views/timing.xml',
        'views/menu.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
    ],
    'license': 'LGPL-3',
}
