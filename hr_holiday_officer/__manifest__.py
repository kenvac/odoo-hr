# -*- coding: utf-8 -*-
# © 2017 Accessbookings Ltd (<http://www.accessbookings.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'HR Officer Access Rights',
    'summary': """ Limits HR officers to their own dapartment""",
    'description': """
Limits access rights for Officers to data regarding employees belonging to
their own department.

* Holidays

    """,
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'author': 'Access Bookings Ltd, Odoo Community Association (OCA)',
    'website': 'http://www.accessbookings.com',
    'depends': ['hr_holidays'],
    'version': '10.0.1.0.0',
    'data': [
        'security/hr_security.xml',
        'views/hr_view.xml',
        'views/hr_holidays_views.xml',
        ],
    'installable': True,
}
