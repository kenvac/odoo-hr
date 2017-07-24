# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'HR Holidays Notification',
    'summary': """Send holiday request email nofitication to
        managers and employees""",
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'author': 'Kinner Vachhani, Odoo Community Association (OCA)',
    'website': 'http://www.odoo-community.org',
    'depends': ['hr_holidays'],
    'version': '10.0.1.0.0',
    'data': [
        'data/hr_holidays_data.xml',
        ],
    'installable': True,
}
