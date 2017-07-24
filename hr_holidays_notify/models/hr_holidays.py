# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class Holidays(models.Model):

    _inherit = 'hr.holidays'

    @api.multi
    def action_confirm(self):
        '''Send holiday approval request email to manager'''
        tmpl = self.env.ref("hr_holidays_notify.hr_holidays_confirm")
        ret_vals = super(Holidays, self).action_confirm()
        # Do not send email when employee is manager
        for holiday in self.filtered(lambda r:
                                     r.type != 'add' and not
                                     r.check_manager() and
                                     r.holiday_status_id.limit):
            tmpl.send_mail(holiday.id)
        return ret_vals

    @api.multi
    def action_approve(self):
        '''Fist level holiday approval'''
        tmpl = self.env.ref("hr_holidays_notify.hr_holidays_approval")
        ret_vals = super(Holidays, self).action_approve()
        # Do not send email when employee is manager
        for holiday in self.filtered(lambda r:
                                     r.type != 'add' and not
                                     r.check_manager() and
                                     r.holiday_status_id.limit):
            tmpl.send_mail(holiday.id)
        return ret_vals

    @api.multi
    def action_validate(self):
        '''Second level holiday approval'''
        tmpl = self.env.ref("hr_holidays_notify.hr_holidays_confirmation")
        ret_vals = super(Holidays, self).action_validate()
        for holiday in self.filtered(lambda r: r.type != 'add' and
                                     r.holiday_status_id.limit):
            tmpl.send_mail(holiday.id)
        return ret_vals

    @api.multi
    def action_refuse(self):
        '''Email on refusal'''
        tmpl = self.env.ref("hr_holidays_notify.hr_holidays_reject")
        ret_vals = super(Holidays, self).action_refuse()
        # Do not send email when employee is manager
        for holiday in self.filtered(lambda r:
                                     r.type != 'add' and not
                                     r.check_manager() and
                                     r.holiday_status_id.limit):
            tmpl.send_mail(holiday.id)
        return ret_vals

    def check_manager(self):
        self.ensure_one()
        dep = self.env['hr.department'].search([('manager_id',
                                                 '=',
                                                 self.employee_id.id)])
        return dep and True or False
