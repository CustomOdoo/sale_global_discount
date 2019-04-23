# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    global_discount = fields.Float('Global Discount')

    @api.onchange('global_discount', 'order_line')
    @api.depends('global_discount')
    def onchange_global_discount(self):
        for line in self.order_line:
            line.discount = self.global_discount