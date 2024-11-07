from odoo import models, fields

class Alumno(models.Model):
    _name = 'colegio.alumno'
    _description = 'Alumno del Colegio'
    _rec_name = 'user_id'

    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    edad = fields.Integer("Edad", required=True)
    tutor_id = fields.Many2one('colegio.tutor', string="Tutor")
    grado = fields.Many2one('colegio.curso', string="Grado Actual")
    curso_ids = fields.Many2many('colegio.curso', through='colegio.inscripcion', string="Cursos")