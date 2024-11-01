from odoo import models, fields

class Inscripcion(models.Model):
    _name = 'colegio.inscripcion'
    _description = 'Inscripción de Alumnos a Cursos'

    fecha_inscripcion = fields.Date('Fecha de Inscripcion')
    alumno_id = fields.Many2one('colegio.alumno', string="Alumno", required=True)
    curso_id = fields.Many2one('colegio.curso', string="Curso", required=True)
    gestion_id = fields.Many2one('colegio.gestion', string="Gestión")  # Nueva relación
