from odoo import models, fields

class Alumno(models.Model):
    _name = 'colegio.alumno'
    _description = 'Alumno del Colegio'

    name = fields.Char("Nombre", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    tutor_id = fields.Many2one('colegio.tutor', string="Tutor")
    curso_ids = fields.Many2many('colegio.curso', through='colegio.inscripcion', string="Cursos")
