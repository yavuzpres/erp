# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name' : 'Reset Manufacturing Order',
    'version' : '13.0',
    'author': 'Biznoways IT Solutions',
    'category': 'Manufacturing',
    'maintainer': 'Biznoways IT Soultions',
    'summary': """Set manufacturing order to Draft when order is cancelled.""",
    'website': 'https://www.biznoways.com',
    'license': 'OPL-1',
    'depends' : ['mrp'],
    'data': [
	    'views/view_manufacturing_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
    'price': 10.00,
    'currency': 'EUR',
    "images":["static/description/Banner.png"],
}
