# -*- coding: utf-8 -*-
###############################################################################
#
# Fortutech IMS Pvt. Ltd.
# Copyright (C) 2016-TODAY Fortutech IMS Pvt. Ltd.(<http://www.fortutechims.com>).
#
###############################################################################
{
    'name': 'Row Number Header Fix Tree View',
    'category': 'Report',
    'summary': 'Show Row Number and Fixed Header in Tree/List View',
    'version': '13.0.1.0',
    'license': 'OPL-1',
    'description': """User allow to see header even there is long scrolling datas, in tree view.""",
    'depends': ['base'],
    'author': "Fortutech IMS Pvt. Ltd.",
    'website': "http://www.fortutechims.com",
    'data': [
        'views/assets.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ['static/description/banner.png'],
}
