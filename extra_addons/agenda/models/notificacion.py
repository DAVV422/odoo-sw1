from odoo import models, fields

class Notificacion(models.Model):
    _name = 'colegio.notificacion'
    _description = 'Notificación'

    title = fields.Char(string='Título', required=True)
    message = fields.Html(string='Mensaje')  # Para texto enriquecido
    date = fields.Date(string='Fecha')
    user_ids = fields.Many2many('res.users', string='Usuarios')
    attachment_ids = fields.Many2many('ir.attachment', string='Archivos Adjuntos', 
                                      help="Adjunta archivos relacionados con la notificación",
                                      relation="m2m_colegio_notificacion_attachment",
                                      domain=[('res_model', '=', 'colegio.notificacion')])

class Lectura(models.Model):
    _name = 'colegio.lectura'
    _description = 'Lectura de Notificaciones por Usuario'

    notificacion_id = fields.Many2one('colegio.notificacion', string="Notificación", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    read = fields.Boolean("Leído", default=False)
