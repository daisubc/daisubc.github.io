---
layout: basic
title: Publications
permalink: /publications/
years: ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002"]
---

**Publication list under construction.** 

Please see [Google Scholar](https://scholar.google.com/citations?user=3rB_SGYAAAAJ&hl=en&oi=ao) for a full list of publications.

---

<div class="tabs">
  <ul>
    <li class="is-active"><a href="{{ site.baseurl }}/publications/">All</a></li>
    <li><a href="{{ site.baseurl }}/publications/papers">Papers</a></li>
    <li><a href="{{ site.baseurl }}/publications/conference">Conference</a></li>
    <li><a href="{{ site.baseurl }}/publications/patents">Patents</a></li>
  </ul>
</div>

<ol reversed class="list is-hoverable">
	{% for y in page.years %}
	{% assign pubs = site.data.publications | where:"year", y %}	
	{% if pubs.size > 0 %}
		<h5 class="list-item" style="background-color: #eee;"><strong>{{y}}</strong></h5>
	{% endif %}
	{% for pub in pubs %}
	<li class="list-item" style="display: list-item">
		{% if pub.type == "paper" %}
			<i>Journal Paper</i>
		{% elsif pub.type == "conference" %}
			<i>Conference Proceedings</i>
		{% elsif pub.type == "patent" %}
			<i>Patent</i>						
		{% endif %}
		<br>

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
	{% endfor %}
</ol>