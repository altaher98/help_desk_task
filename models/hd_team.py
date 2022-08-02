# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hdTeam(models.Model):
    _name = "hd.team"
    _description = " HD Team "
    _rec_name = 'name'

    name = fields.Char("Name", required=True)
