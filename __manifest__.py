{
    "name": "Pizza",
    "version": "17.0",
    "category": "",
    "summary": "Summary",
    "description": """ Description """,
    "depends": [
        "web",
        # "purchase",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/pizza_main_page_data.xml",
        "views/pizza_main_page_views.xml",
        "views/pizza_pizza_views.xml",
        "views/cart_views.xml",
        "views/pizza_configurator_views.xml",
        "views/pizza_type_views.xml",
        "views/drink_views.xml",
    ],
    # "assets": {
    #     "web.assets_backend": [
    #         "todo/static/src/**/*",
    #     ],
    # },
    'assets': {
        'web.assets_backend': [
            'pizza/static/src/js/pizza_cart.js',
            # "pizza/static/src/js/view_service.js",
            'pizza/static/src/xml/pizza_cart.xml',
            'pizza/static/src/css/pizza_main_page.css',

        ],
    },
    "application": True,
}
