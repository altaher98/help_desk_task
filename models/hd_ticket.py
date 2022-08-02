# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime , date
from odoo.exceptions import AccessError, UserError, ValidationError



class hdTicket(models.Model):
    _name = "hd.ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = " hd ticket "
    _rec_name = 'name'

    name = fields.Char(string='Name',required=True, copy=False, readonly=True,
                                index=True, default=lambda self: _('New'), ondelete='cascade')
    description = fields.Text(string='Description',required=True)
    team = fields.Many2one('hd.team',string='Team',required=True,tracking=True)
    assigned = fields.Many2one('res.users',string='Assigned',required=True)
    priority = fields.Selection([
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High')], string="Priority")
    tags = fields.Many2many('hd.tags',string='Tags',required=True)
    customer_name = fields.Many2one('res.partner',string='Customer name',required=True,tracking=True)
    customer_email = fields.Char(related='customer_name.email',string='Customer email')
    customer_phone = fields.Char(related='customer_name.phone',string='Customer phone')
    hosting_type = fields.Selection([
        ('on_premise', 'On-Premise'),
        ('cloud', 'Cloud')], string='Hosting type',required=True)
    server_url = fields.Char(string='Server URL')
    resolution_time = fields.Date(string='Resolution time',required=True, tracking=True)
    state = fields.Selection([
        ('new', 'New'),
        ('progress', 'Progress'),
        ('solved', 'Solved'),
        ('cancel', 'Cancelled'),
    ], string='Status', index=True, readonly=True, copy=False, default='new', tracking=True)
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hd.ticket') or 'New'
        result = super(hdTicket, self).create(vals)
        return result

    def unlink(self):
        for order in self:
            if order.state != 'new':
                raise UserError(_('Cannot delete not New'))
        return super(hdTicket, self).unlink()

    def action_progress(self):
        self.write({'state': 'progress'})

    def action_solved(self):
        self.write({'state': 'solved'})

    def action_cancel(self):
        self.write({'state': 'cancel'})
