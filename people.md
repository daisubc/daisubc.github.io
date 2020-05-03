---
layout: basic
title: People
description: Meet the UBC DAIS Lab team. Our research group is working on machine learning, data analytics and process control research.
permalink: /people/
---

# Faculty & Staff
- **[Dr. Bhushan Gopaluni]({{ site.baseurl }}/about/)**, Principal Investigator
- **[Aleli Capuno](https://engineering.ubc.ca/about/staff-directory)**, Admin Assistant to Associate Deans

{% assign degrees = "Postdoc|PhD|MASc|Undergraduate" | split: "|" %}
{% for degree in degrees %}

<h1 class="title"> {{ degree }} </h1>
{% assign members = site.data.members | where:"degree", degree | sort: 'year_start' | reverse %}

<div>
	{% for member in members %}
	<div class="is-clearfix">
        <figure class="image is-round is-128x128 is-pulled-left">
        	{% if member.img %}
        	<img class="is-rounded" style="height: 100%; object-fit: cover;" src="{{ site.baseurl }}/assets/profile/{{ member.img }}">
        	{% else %}
        	<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" alt="Placeholder image">
        	{% endif %}
        </figure>
        <div class="content">
			<p class="title is-size-5-mobile">
			{% if member.has_profile %}
				<a href="{{ site.baseurl }}/profile/{{ member.name }}">{{ member.name }}</a>
			{% else %}
				{{ member.name }}
			{% endif %}
			<br>
			<p class="subtitle is-size-7 is-size-7-mobile is-size-6">
				Started {{ member.year_start }}
			{% if member.cosupervisor %}
				| Co-supervisor: {{ member.cosupervisor }}
			{% endif %}							
			</p>
			</p>
			<p class="subtitle is-size-6 is-size-7-mobile">{{ member.project }}
			{% if member.project_url %}
			<a href="{{ site.baseurl }}/{{ member.project_url }}"><span class="tag is-light is-info">PDF</span></a>
			{% endif %}</p>
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
			<th>Position After Leaving/Now At</th>
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