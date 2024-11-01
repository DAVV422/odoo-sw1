from odoo import models, fields

class Tutor(models.Model):
    _name = 'colegio.tutor'
    _description = 'Tutor o Apoderado'
    

    name = fields.Char("Nombre", required=True)
    relationship = fields.Char("Parentesco Familiar", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    alumno_ids = fields.One2many('colegio.alumno', 'tutor_id', string="Alumnos")
