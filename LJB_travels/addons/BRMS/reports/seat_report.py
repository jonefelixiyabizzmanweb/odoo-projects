from odoo import models, fields, api


class SeatReport(models.AbstractModel):
    _name = 'report.brms.reservation_seat_template'

    def _get_report_values(self, docids, data=None):
        docs = self.env['reservation.details'].browse(data['reservation_id'])
        print(docs)
        return {
            'docs': docs,
        }