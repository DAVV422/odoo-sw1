from odoo import models, fields

class Curso(models.Model):
    _name = 'colegio.curso'
    _description = 'Curso del Colegio'
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre del Curso", required=True)
    nivel = fields.Char("Nivel del Curso", required=True)
    alumno_ids = fields.Many2many('colegio.alumno', through='colegio.inscripcion', string="Alumnos")
    asignacion_ids = fields.One2many('colegio.asignacion', 'curso_id', string="Asignaciones")
    
    #Función para mostrar el nombre y el nivel en el _rec_name
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nombre} - {record.nivel}" if record.nivel else record.nombre
            result.append((record.id, name))
        return result
