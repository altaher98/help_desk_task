# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hdTags(models.Model):
    _name = "hd.tags"
    _description = " HD Tags "
    _order = "name"

    name = fields.Char("Name", required=True)
    color = fields.Integer('Color Index', default=1)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
