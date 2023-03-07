{
    'name': 'YavuzPres Sale MRP Intercompany',
    'summary': 'Create intercompany manufacturing orders from sale orders',
    'version': '13.0.1.0.0',
    'category': 'Sale',
    'author': 'YavuzPres',
    'website': 'http://www.yavuzpres.com.tr',
    'license': 'AGPL-3',
    'depends': [
        'mrp',
        'sale',
    ],
    'data': [
        'views/mrp_production_view.xml',
        'views/res_company_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_type_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
