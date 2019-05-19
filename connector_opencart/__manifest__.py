# © 2019 Hibou Corp.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Opencart Connector',
    'version': '12.0.1.0.0',
    'category': 'Connector',
    'depends': [
        'account',
        'product',
        'delivery',
        'sale_stock',
        'connector_ecommerce',
    ],
    'author': 'Hibou Corp.',
    'license': 'AGPL-3',
    'website': 'https://hibou.io',
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_views.xml',
        'views/opencart_backend_views.xml',
    ],
    'installable': True,
    'application': False,
}
