---
layout: basic
title: Publications
permalink: /publications/
---

**Publication list under construction.** 

Please see [Google Scholar](https://scholar.google.com/citations?user=3rB_SGYAAAAJ&hl=en&oi=ao) for a full list of publications.

---

#### Jump to
[Papers](#paper) | [Conferences](#conference) | [Patents](#patent)

{% assign papertypes = "paper|conference|patent" | split: "|" %}
{% for papertype in papertypes %}
{% assign papers = site.data.publications | where:"type", papertype %}

## {{ papertype | capitalize}} 
<a href="#"><span class="tag is-small is-light">Back to Top</span></a>

<ol reversed class="list is-hoverable">
	{% for pub in papers %}
	<li class="list-item" style="display: list-item">
		<b class="large">{{ pub.title }}</b><br>
		{{ pub.authors }}<br>
		<i>
		{% if pub.url %}
		<a href="{{ pub.url }}" target="_blank">
			{{ pub.journal }}.
		</a>
		{% else %}
		{{ pub.journal }}.
		{% endif %}
		</i>
		{{ pub.year }}

		{% if pub.pdf %}
		<a href="{{ site.baseurl }}/assets/preprints/{{ pub.pdf }}"><span class="tag is-info">[PDF]</span></a>
		{% endif %}	

		{% if pub.slides %}
		<a href="{{ site.baseurl }}/assets/preprints/{{ pub.slides }}"><span class="tag is-warning">[Slides]</span></a>
		{% endif %}		

		{% if pub.code %}
		<a href="{{ pub.code }}"><span class="tag is-success">[Code]</span></a>
		{% endif %}					

		{% if pub.notes %}
		<br>
		<span class="tag is-info is-light">{{ pub.notes }}</span>
		{% endif %}			

	</li>
	{% endfor %}
</ol>

{% endfor %}