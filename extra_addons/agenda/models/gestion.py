from odoo import models, fields

class Gestion(models.Model):
    _name = 'colegio.gestion'
    _description = 'Gestión de Inscripciones y Asignaciones'

    name = fields.Char("Nombre de la Gestión", required=True)
    date_start = fields.Date('Fecha de Inicio', required=True)
    date_end = fields.Date('Fecha Finalización')
    inscripcion_ids = fields.One2many('colegio.inscripcion', 'gestion_id', string="Inscripciones")
    asignacion_ids = fields.One2many('colegio.asignacion', 'gestion_id', string="Asignaciones")
