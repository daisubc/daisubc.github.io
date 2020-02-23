---
layout: basic
title: Publications
permalink: /publications/
---

<ol>
	{% for pub in site.data.publications %}
	<li>
		<b><span class="pub-title">{{ pub.title }}</span></b><br>
		<span class="pub-authors">{{ pub.authors }}</span><br>
		<span class="pub-url"><i><a href="{{ pub.url }}" target="_blank">{{ pub.journal }}.</a></i> {{ pub.date }}</span>
	</li>
	{% endfor %}
</ol>