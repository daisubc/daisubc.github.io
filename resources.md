---
layout: basic
title: Resources
permalink: /resources/
---

<div class="table-container">
<table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
	<thead>
		<tr>
			<th>Title</th>
			<th>Author(s)</th>
			<th>Date</th>
			<th>Download</th>
		</tr>
	</thead>
	<tbody>
		{% assign resources = site.data.resources %}
		{% for resource in resources %}
		<tr>
			<td>
				{% if resource.url %}
					<a target="_blank" href="{{ resource.url }}">{{ resource.title }}</a>
				{% else %}
					{{ resource.title }}
				{% endif %}
			</td>
			<td>{{ resource.authors | array_to_sentence_string }}</td>
			<td>{{ resource.date | date_to_long_string }}</td>
			<td>
				{% if resource.filename %}
					<a target="_blank" href="{{ site.baseurl }}/assets/pdf/{{ resource.filename }}">{{ resource.filename }}</a>
				{% else %}
					-
				{% endif %}
			</td>
		</tr>
		{% endfor %} 
	</tbody>
</table>
</div>