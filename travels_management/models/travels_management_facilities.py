from odoo import fields, models


class Facilities(models.Model):
    _name = "travels.management.facilities"
    _description = "travels management facilities"
    name = fields.Char()
