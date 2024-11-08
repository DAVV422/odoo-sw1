from odoo import models, fields, api

class Tutor(models.Model):
    _name = 'colegio.tutor'
    _description = 'Tutor o Apoderado'
    _rec_name = 'user_id'
    
    parentesco = fields.Char("Parentesco Familiar", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    alumno_ids = fields.One2many('colegio.alumno', 'tutor_id', string="Alumnos")