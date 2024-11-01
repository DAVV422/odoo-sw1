from odoo import models, fields

class Administrativo(models.Model):
    _name = 'colegio.administrativo'
    _description = 'Personal Administrativo del Colegio'

    name = fields.Char("Nombre", required=True)
    position = fields.Char("Cargo", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
