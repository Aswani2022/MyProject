from odoo import fields, models


class ServiceTypes(models.Model):
    _name = "travels.management.service.types"
    _description = "travels management service types"
    name = fields.Char(string="Name")
    expiration_period = fields.Integer(string="Expiration period")
    service_id = fields.Many2one("travels.management.vehicle")
    service = fields.Char()
    quantity = fields.Integer(default='1', readonly=True)
    unit = fields.Integer()
    amount = fields.Integer()


