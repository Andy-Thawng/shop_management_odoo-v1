{
    "name" : "Shop Management",
    "version" : "1.0",
    "author" : "Andy Thawng",
    "category" : "Sales",
    "summary": "Simple Shop Management System",
    "description": """
        This module helps to manage a shop's operations, including inventory, sales, and customer management.
    """,
    "depends" : ["product"],
    "data" : [
        'views/shop_item_views.xml',
        'views/shop_menu_views.xml',
        'security/ir.model.access.csv'
    ],
    "installable": True,
    "application": True,
    "license": "AGPL-3"
}