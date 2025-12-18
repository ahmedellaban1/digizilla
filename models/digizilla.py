from odoo import models, fields


class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Required Fields
    name = fields.Char(string='Name', required=True, tracking=True)
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        tracking=True,
        default=lambda self: self.env.company
    )

    # Optional Fields
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        string='Gender',
        tracking=True
    )
    
    country_id = fields.Many2one(
        'res.country',
        string='Country',
        tracking=True
    )
    
    joining_date = fields.Date(string='Joining Date', tracking=True)
    
    tag_ids = fields.Many2many(
        'res.partner.category',
        string='Tags',
        tracking=True
    )
    
    customer_ids = fields.Many2many(
        'res.partner',
        'digizilla_customer_rel',
        'digizilla_id',
        'customer_id',
        string='Customers',
        tracking=True
    )

    notes = fields.Text(string='Notes', tracking=True)
    
    comments = fields.Char(string='Comments', tracking=True)