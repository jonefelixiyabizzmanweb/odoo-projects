from odoo import api, fields, models


class ReservationReport(models.AbstractModel):
    _name = 'report.brms.reservation_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['reservation.details'].browse(data['reservstion_ids'])
        print(docs)
        return {
            'docs': docs,
        }
