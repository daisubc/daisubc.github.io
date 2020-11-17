---
layout: basic
title: People
description: Meet the UBC DAIS Lab team. Our research group is working on machine learning, data analytics and process control research.
permalink: /people/
years: ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002"]
---

{% assign active_members = site.profiles | where_exp:"member", "member.status != 'alumni'" %}
{% assign degrees = "Research Associate|Postdoc|PhD|MASc|MEng|Undergraduate" | split: "|" %}

<h1 class="title">Faculty & Staff</h1>
- **[Bhushan Gopaluni]({{ site.baseurl }}/about/)**, Principal Investigator
- **[Link to APSC Staff Directory](https://engineering.ubc.ca/about/staff-directory)**

{% for degree in degrees %}

<h1 class="title"> {{ degree }} </h1>
<!-- Github pages is still at jekyll 3.9.0, doesnt support binary operators in where_exp yet -->
{% assign members = active_members | where_exp:"member", "member.degree == degree" | sort: 'year_start' | reverse %}

<div class="columns is-multiline">
{% for member in members %}
	<div class="column is-one-third-desktop is-full-mobile">
		<article class="media">
		  <figure class="media-left">
		    <p class="image is-96x96 is-round">
		    	{% if member.img %}
		    		<a href="{{ member.url }}"><img class="is-rounded" style="height: 100%; object-fit: cover;" src="{{ site.baseurl }}/assets/profile/{{ member.img }}" alt="{{ member.title }}"></a>
		    	{% else %}
		    		<a href="{{ member.url }}"><img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" alt="Placeholder Profile Image"></a>
		    	{% endif %}	    	
		    </p>
		  </figure>
	  	<div class="media-content">
	    	<div class="content">	  
		  		<b><a href="{{ member.url }}"><span itemprop="name">{{ member.title }}</span></a></b>
		  		<p><small>{{ member.project }}</small></p>
		  	</div>
		  </div>
		</article>
	</div>
{% endfor %}
</div>

{% endfor %}

<h1> Alumni </h1>
<p> Former students and visitors </p>

<div class="table-container">
<table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
	<thead>
		<tr>
			<th>Name</th>
			<th>Degree</th>
			<th>Position After Leaving/Now At</th>
		</tr>
	</thead>
	<tbody>	
	{% for y in page.years %}
		{% assign sorted_alum = site.data.alumni | where:"year", y %}	
		{% if sorted_alum.size > 0 %}
			<td colspan="3" style="background-color: #eee;"><b>{{y}}</b></td>
			{% for alum in sorted_alum %}
				<tr>
					<td>{% if alum.url %}
						<a href="{{ alum.url }}">{{ alum.name }}</a>
						{% else %}
						{{ alum.name }}
						{% endif %}
					</td>
					<td>{{ alum.degree }}</td>
					<td>{{ alum.position }}</td>
				</tr>
			{% endfor %} 
		{% endif %}
	{% endfor %}
	</tbody>
</table>	
</div>

<small><sup>*</sup><i>My collaborators formally supervised these students but I played a significant role in guiding the research of the respective students.</i></small>

{% include awards.html %}