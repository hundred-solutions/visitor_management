from odoo import fields, models


class VisitorReport(models.TransientModel):
    _name = 'visitor.report.wizard'

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def visitor_report(self):
        check_in_data = self.env['visit.data'].search([('check_in_date', '>=', self.date_from),
                                                       ('check_in_date', '<=', self.date_to)])
        for data in check_in_data:
            datas = {
                'name': data.v_name.v_name
            }
            print("datas", datas)
        return self.env.ref('visitor_management.visitor_report_action').report_action(self, data=datas)
