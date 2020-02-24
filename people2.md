---
layout: people2
title: People
permalink: /people2/
---

# Faculty & Staff
- **[Dr. Bhushan Gopaluni]({{ site.baseurl }}/about/)**, Principal Investigator
- **[Aleli Capuno](https://engineering.ubc.ca/staff/aleli-capuno)**, Admin Assistant to Associate Deans

# Postdocs

<ul>
	{% for member in site.data.members %}
	{% if member.degree == 'PDF' %}
	<li><b>{{ member.name }}</b><br>{{ member.project }}</li>
	{% endif %}
	{% endfor %} 
</ul>

# PhD

<ul>
	{% for member in site.data.members %}
	{% if member.degree == 'PhD' %}
	<li>
		<b>
		{% if member.has_profile %}
			<a href="{{ site.baseurl }}/profile/{{ member.name }}">{{ member.name }}</a>
		{% else %}
			{{ member.name }}
		{% endif %}
		</b>
		<br>{{ member.project }}
	</li>
	{% endif %}
	{% endfor %} 
</ul>

# MASc

<ul>
	{% for member in site.data.members %}
	{% if member.degree == 'MASc' %}
	<li><b>{{ member.name }}</b><br>{{ member.project }}</li>
	{% endif %}
	{% endfor %} 
</ul>

# Undergraduate

<ul>
	{% for member in site.data.members %}
	{% if member.degree == 'Undergraduate' %}
	<li><b>{{ member.name }}</b><br>{{ member.project }}</li>
	{% endif %}
	{% endfor %} 
</ul>


# Alumni 
#### Former students and visitors

<div class="table-container">
<table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
	<thead>
		<tr>
			<th>Name</th>
			<th>Year</th>
			<th>Degree</th>
			<th>Now At</th>
		</tr>
	</thead>
	<tbody>
		{% assign sorted_alum = site.data.alumni | sort: 'year' | reverse %}
		{% for alum in sorted_alum %}
		<tr>
			<td>{% if alum.url %}
				<a href="{{ alum.url }}">{{ alum.name }}</a>
				{% else %}
				{{ alum.name }}
				{% endif %}
			</td>
			<td>{{ alum.year }}</td>
			<td>{{ alum.degree }}</td>
			<td>{{ alum.position }}</td>
		</tr>
		{% endfor %} 
	</tbody>
</table>
</div>