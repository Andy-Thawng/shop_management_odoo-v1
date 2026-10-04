from odoo import models, fields, api

class ShopItem(models.Model):
    _name = 'shop.item' #model_shop_item or table => shop_item
    _description = 'Shop Item'

    name = fields.Char(string='Name', required=True)
    number = fields.Integer(string='Item Reference', required=True)
    quantity = fields.Float(string='Stock Quantity')
    is_available = fields.Boolean(string='Is Available', compute='_compute_is_available')
    date = fields.Date(string='Date')
    receive_date = fields.Datetime(string='Receive Date')
    state = fields.Selection(selection=[('draft', 'Draft'), ('available', 'Available'), ('sold', 'Sold')], string='State', default='draft')
    currency_id = fields.Many2one('res.currency', string='Currency')
    tag_ids = fields.Many2many('shop.item.tag', 
                                'shop_item_tag_rel',
                                 string='Tags' )
    item_line_ids = fields.One2many('shop.item.line', 'item_id', string='Item Lines')

    @api.depends('quantity')
    def _compute_is_available(self):
        for record in self:
            if record.quantity > 0:
                record.is_available = True
            else:
                record.is_available = False

    def action_confirm(self):
        self.state = 'available'

    def action_sold(self):
        self.state = 'sold'

class ShopItemTag(models.Model):
    _name = 'shop.item.tag' #model_shop_item_tag or table => shop_item_tag
    _description = 'Shop Item Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color')

class ShopItemLine(models.Model):
    _name = 'shop.item.line'
    _description = 'Shop Item Line'

    item_id = fields.Many2one('shop.item', string='Item')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    unit_cost = fields.Float(string='Unit Cost')
    total_cost = fields.Float(string='Total Cost')

    @api.onchange('quantity', 'unit_cost')
    def _compute_total_cost(self):
        # import pdb
        # pdb.set_trace()
        self.total_cost = self.quantity * self.unit_cost
    



