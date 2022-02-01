
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api


class Booking(models.Model):
    _name = "travels.management.booking"
    _description = "travels management booking"

    def _compute_expiration_date(self):
        print(self)
        for rec in self:
            rec.expiration_date = rec.booking_date + relativedelta(
                days=int(rec.services_id.expiration_period))
            if rec.expiration_date < fields.Date.today():
                rec.write({'state': 'expired'})

    def button_confirmed(self):
        # print(self.customer_id.name)
        self.write({'state': 'confirmed'})

    def button_reset(self):
        self.write({'state': 'draft'})

    def button_cancel(self):
        self.write({'state': 'cancelled'})

    name = fields.Char(string="Booking Reference", readonly=True, required=True,
                       copy=False, default='New')
    customer_id = fields.Many2one("res.partner", string="Customer", copy=False)

    no_of_passengers = fields.Integer(string="No of Passengers", default='1')

    # service = fields.Selection(
    #     string='Service',
    #     selection=[('flight', 'Flight'), ('train', 'Train'), ('bus', 'Bus')],
    #     help="service is used to separate Flight,Train and Bus")
    services_id = fields.Many2one("travels.management.service.types",
                                  required=True)
    booking_date = fields.Date(default=fields.Date.context_today)
    source_location_id = fields.Many2one("travels.management.location")
    destination_location_id = fields.Many2one("travels.management.location")

    travel_date = fields.Datetime()
    expiration_date = fields.Date(compute=_compute_expiration_date)
    # current_date = fields.Date(default=fields.Date.context_today)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ], default="draft")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'booking') or 'New'
        result = super(Booking, self).create(vals)
        return result
