# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MemesCorner(models.Model):
    _name = "memes.corner"

    name = fields.Char('Image Name')
    image = fields.Binary("Image")
    categ_id = fields.Many2one('memes.categ', string='Category')
    likes = fields.Integer(string='Likes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('review', 'In-Review'),
        ('done', 'Done')
    ], default='draft', string='State')

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):

        res = super(MemesCorner, self).search_read(domain=None, fields=None, offset=0, limit=None, order=order)
        print("callllllllllllllllllllllllllllllllllll", res)
        return res


class MemesCateg(models.Model):
    _name = "memes.categ"

    name = fields.Char('Name')
