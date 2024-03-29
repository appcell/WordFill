from django.conf import settings
settings.configure()

from django import template
from django.template import Context, Template

 from django.template import Template, Context
 raw_template = """<p>Dear {{ person_name }},</p>

 <p>Thanks for ordering {{ product }} from {{ company }}. It's scheduled to
 ship on {{ ship_date|date:"F j, Y" }}.</p>

 {% if ordered_warranty %}
 <p>Your warranty information will be included in the packaging.</p>
 {% endif %}

 <p>Sincerely,<br />{{ company }}</p>"""
 t = Template(raw_template)
 import datetime
 c = Context({'person_name': 'John Smith',
     'product': 'Super Lawn Mower',
     'company': 'Outdoor Equipment',
     'ship_date': datetime.date(2009, 4, 2),
     'ordered_warranty': True})
 t.render(c)
