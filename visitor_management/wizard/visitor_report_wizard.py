from odoo import fields, models


class VisitorReport(models.TransientModel):
    _name = 'visitor.report.wizard'

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def visitor_report(self):
        check_in_data = self.env['visit.data'].search([('check_in_date', '>=', self.date_from),
                                                       ('check_in_date', '<=', self.date_to)])
        print("check", check_in_data)
        name_list = []
        refrence_employee = []
        for data in check_in_data:
            name_list.append(data.v_name.v_name)
            refrence_employee.append(data.employee_id.name)

        data = {
            'name': name_list,
            'refrence_emp': refrence_employee
        }

        print("datas", data)
        return self.env.ref('visitor_management.visitor_report_action').report_action(self, data=data)
