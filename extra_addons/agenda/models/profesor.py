from odoo import models, fields

class Profesor(models.Model):
    _name = 'colegio.profesor'
    _description = 'Profesor del Colegio'
    _rec_name = 'user_id'

    especialidad = fields.Char("Especialidad", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    asignacion_ids = fields.One2many('colegio.asignacion', 'profesor_id', string="Asignaciones")
