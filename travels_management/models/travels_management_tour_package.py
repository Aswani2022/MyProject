from odoo import fields, models, api


class TourPackage(models.Model):
    _name = "tour.package"
    _description = "tour package"

    customer_id = fields.Many2one("res.partner", string="Customer")
    quotation_date = fields.Date(string="Date")
    source_location_id = fields.Many2one("travels.management.location")
    destination_location_id = fields.Many2one("travels.management.location")
    start_date = fields.Date()
    end_date = fields.Date()
    no_of_travellers = fields.Integer(string="No of Travellers")
    facilities_ids = fields.Many2many("travels.management.facilities",
                                      string="Facilities")
    vehicle_type = fields.Selection([
        ('bus', 'Bus'),
        ('traveller', 'Traveller'),
        ('van', 'Van'),
        ('other', 'Other')
    ])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
    ], default="draft")

