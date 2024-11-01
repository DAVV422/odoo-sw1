from odoo import models, fields

class Materia(models.Model):
    _name = 'colegio.materia'
    _description = 'Materia del Colegio'

    name = fields.Char("Nombre de la Materia", required=True)
    description = fields.Char("Descripcion de la materia", required=True)
    asignacion_ids = fields.One2many('colegio.asignacion', 'materia_id', string="Asignaciones")
