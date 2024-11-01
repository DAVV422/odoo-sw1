from odoo import models, fields

class Curso(models.Model):
    _name = 'colegio.curso'
    _description = 'Curso del Colegio'

    name = fields.Char("Nombre del Curso", required=True)
    level = fields.Char("Nivel del Curso", required=True)
    alumno_ids = fields.Many2many('colegio.alumno', through='colegio.inscripcion', string="Alumnos")
    asignacion_ids = fields.One2many('colegio.asignacion', 'curso_id', string="Asignaciones")
