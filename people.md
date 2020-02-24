---
layout: basic
title: People
permalink: /people/
---

# Faculty & Staff
- **[Dr. Bhushan Gopaluni]({{ site.baseurl }}/about/)**, Principal Investigator
- **[Aleli Capuno](https://engineering.ubc.ca/staff/aleli-capuno)**, Admin Assistant to Associate Deans

{% assign degrees = "Postdoc|PhD|MASc|Undergraduate" | split: "|" %}
{% for degree in degrees %}

<h1 class="title"> {{ degree }} </h1>
{% assign members = site.data.members | where:"degree", degree %}

<div>
	{% for member in members %}
	<div class="is-clearfix">
        <figure class="image is-round is-128x128 is-pulled-left">
        	{% if member.img %}
        	<img class="is-rounded" style="height: 100%; object-fit: cover;" src="{{ site.baseurl }}/{{ member.img }}">
        	{% else %}
        	<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" alt="Placeholder image">
        	{% endif %}
        </figure>
        <div class="content">
			<p class="title">
			{% if member.has_profile %}
				<a href="{{ site.baseurl }}/profile/{{ member.name }}">{{ member.name }}</a>
			{% else %}
				{{ member.name }}
			{% endif %}
			</p>
			<p class="subtitle">{{ member.project }}</p>
		</div>
	</div>
	{% endfor %}
</div>
{% endfor %}

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