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
			<td>{{ resource.title }}</td>
			<td>{{ resource.authors | array_to_sentence_string }}</td>
			<td>{{ resource.date | date_to_long_string }}</td>
			<td><a target="_blank" href="{{ site.baseurl }}/assets/pdf/{{ resource.filename }}">{{ resource.filename }}</a></td>
		</tr>
		{% endfor %} 
	</tbody>
</table>
</div>