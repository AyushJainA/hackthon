# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Ksquare Customization',
    'version': '17.0',
    'author': 'Odoo PS',
    'odoo_task_id': "4218574",
    'category': 'Customization',
    'license': 'LGPL-3',
    'summary': 'Ksquare SO and PO duplicate custom',
    'depends': ['sale','purchase','base_automation'],
    'data': [
        'data/base_automation.xml',
    ],
    'installable': True,
    'auto_install': False,
}
