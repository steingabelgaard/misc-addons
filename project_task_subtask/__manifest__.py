# -*- coding: utf-8 -*-
{
    "name": """Project Task Checklist""",
    "summary": """Use checklist to be ensure that all your tasks are performed and to make easy control over them""",
    "category": """Project Management""",
    "images": ['images/checklist_main.png'],
    "version": "10.0.1.0.3",
    "application": False,

    "author": "IT-Projects LLC, Manaev Rafael",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "GPL-3",
    "price": 69.00,
    "currency": "EUR",

    "depends": ['base', 'project'],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/ir.model.access.csv',
        'views/project_task_subtask.xml',
        'data/subscription_template.xml',
        'security/project_security.xml'
    ],
    "qweb": [
    ],
    "demo": [
        'demo/project_task_subtask_demo.xml'
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
