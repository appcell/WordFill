{% for item in main %}
<li>{{ item }}</li>
{% endfor %}

<a href="/query/{{ newword }}/">next: {{ newword }}</a>