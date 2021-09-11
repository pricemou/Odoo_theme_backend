# -*- coding: utf-8 -*-
{
    'name':
    "Css",
    'Construction':
    """
        Theme de construction""",
    'description':
    """
       css.
    """,
    'author':
    "Pricemou Claude",
    'website':
    "http://www.AfricaDevTalents.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Theme',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website','website_theme_install'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
