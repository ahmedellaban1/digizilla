{
    'name': 'Digizilla',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Digizilla Management',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'reports/digizilla_report.xml',
        'reports/digizilla_report_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'Digizilla/static/src/js/digizilla_form.js',
        ],
    },
    'installable': True,
    'application': True,
}