from odoo import fields, models


class Location(models.Model):
    _name = "travels.management.location"
    _description = "travels management location"
    name = fields.Char()
