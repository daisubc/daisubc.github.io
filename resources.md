---
layout: basic
title: Resources
permalink: /resources/
description: Resources available from the DAIS Lab research group at UBC. We post slides, presentations and workshop materials on advanced process control, data analytics and machine learning.
---

Videos and presentations are available in our [Vimeo](https://vimeo.com/showcase/7521351){:target="_blank"} page. Posters and other documents are also available in our [Figshare](https://figshare.com/authors/Bhushan_Gopaluni/9643466) page.

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