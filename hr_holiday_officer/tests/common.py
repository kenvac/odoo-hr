# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestHrHolidaysBase(common.TransactionCase):

    def setUp(self):
        super(TestHrHolidaysBase, self).setUp()

        Users = self.env['res.users'].with_context(no_reset_password=True)

        # Find groups
        group_employee_id = self.ref('base.group_user')
        group_hr_officer_id = self.ref('hr.group_hr_user')
        group_hr_manager_id = self.ref('hr_holidays.group_hr_holidays_manager')
        group_holiday_officer_id = self.\
            ref('hr_holidays.group_hr_holidays_user')
        group_holiday_manager_id = self.\
            ref('hr_holidays.group_hr_holidays_manager')

        dep_it = self.env['hr.department'].create({
            'name': 'Information Technology',
        })
        self.dep_it = dep_it.id
        # Test users to use through the various tests
        # Employee
        self.user_employee_id = Users.create({
            'name': 'Kane Employee',
            'login': 'kane',
            'email': 'kane.employee@example.com',
            'groups_id': [(6, 0, [group_employee_id])]
        }).id
        # Employee Manager
        self.user_manager_id = Users.create({
            'name': 'Daniel Manager',
            'login': 'dan',
            'email': 'dan.manager@example.com',
            'groups_id': [(6, 0, [group_holiday_officer_id,
                                  group_hr_officer_id])]
        }).id
        # HR Manager
        self.user_hrmanager_id = Users.create({
            'name': 'Scott HrManager',
            'login': 'scott',
            'email': 'scot.hrmanager@example.com',
            'groups_id': [(6, 0, [group_hr_manager_id,
                                  group_holiday_manager_id])]
        }).id
        # HOD
        self.employee_manager_id = self.env['hr.employee'].create({
            'name': 'Daniel Manager',
            'user_id': self.user_manager_id,
            'department_id': self.dep_it,
        }).id
        # Hr Data
        self.employee_emp_id = self.env['hr.employee'].create({
            'name': 'Kane Employee',
            'user_id': self.user_employee_id,
            'department_id': self.dep_it,
        }).id
        # Assign HOD to department
        dep_it.manager_id = self.employee_manager_id
