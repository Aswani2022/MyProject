from odoo import fields, models, api


class Vehicle(models.Model):
    _name = "travels.management.vehicle"
    _description = "travels management vehicle"

    def _compute_name(self):
        for rec in self:
            rec.name = rec.registration_no + rec.vehicle_type


    registration_no = fields.Char(string="Registration NO.",
                       help='Unique number written on the vehicle',
                       required=True, copy=False)
    _sql_constraints = [
        ('field_unique',
         'unique(registration_no)',
         'Choose another value - it has to be unique!')
    ]

    vehicle_type = fields.Selection([
        ('bus', 'Bus'),
        ('traveller', 'Traveller'),
        ('van', 'Van'),
        ('other', 'Other')
    ])
    name = fields.Char(compute=_compute_name)
    no_of_seats = fields.Integer(default='1')
    facilities_ids = fields.Many2many("travels.management.facilities")
    service_ids = fields.One2many("travels.management.service.types", "service_id")

    date_request = fields.Date()
    return_date = fields.Date()

