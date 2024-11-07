from odoo import models, fields, api

class Administrativo(models.Model):
    _name = 'colegio.administrativo'
    _description = 'Personal Administrativo del Colegio'
    _rec_name = 'user_id'

    posicion = fields.Char("Cargo", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
