# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'altaher_help_desk',
    'version' : '1.1',
    'summary': '',
    'sequence': 90,
    'description': """
    """,
    'category': '',
    'website': '',
    'depends' : ['base','mail','contacts'],
    'data': [
        'security/help_desk_security.xml',
        'security/ir.model.access.csv',
        'views/hd_tags.xml',
        'views/hd_team.xml',
        'views/hd_ticket.xml',
        'data/sequence.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
