---
layout: basic
title: People
description: Meet the UBC DAIS Lab team. Our research group is working on machine learning, data analytics and process control research.
permalink: /people/
years: ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002"]
---

# Faculty & Staff
- **[Dr. Bhushan Gopaluni]({{ site.baseurl }}/about/)**, Principal Investigator
- **[Aleli Capuno](https://engineering.ubc.ca/about/staff-directory)**, Admin Assistant to Associate Deans

{% assign degrees = "Research Associate|Postdoc|PhD|MASc|MEng|Undergraduate" | split: "|" %}
{% for degree in degrees %}

<h1 class="title"> {{ degree }} </h1>
{% assign members = site.data.members | where:"degree", degree | sort: 'year_start' | reverse %}

<div>
	<div class="columns is-multiline is-mobile is-fullheight">
	{% for member in members %}
	<div class="column is-half-desktop is-full-mobile">
		<div class="card" style="display:flex; flex-direction: column; height: 100%;">
			<header class="card-header">
				<p class="card-header-title">
				{% if member.has_profile %}
					<a href="{{ site.baseurl }}/profile/{{ member.name }}">{{ member.name }}</a>
				{% else %}
					{{ member.name }}
				{% endif %}
				</p>
			</header>
			<div id="collapsible-card" class="is-collapsible is-active">
				<div class="card-content">
					<div class="columns is-multiline is-mobile">
						<div class="column is-one-third-desktop">
					    <figure class="image is-round is-128x128">
					    	{% if member.img %}
					    	<img class="is-rounded" style="height: 100%; object-fit: cover;" src="{{ site.baseurl }}/assets/profile/{{ member.img }}">
					    	{% else %}
					    	<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" alt="Placeholder image">
					    	{% endif %}
					    </figure>
					   </div>
					   <div class="column">
					    <p>
					    	<span class="has-text-weight-light is-size-7"><i class="fas fa-envelope"></i> {{ member.email }}</span><br>
					    	<small>
									Started {{ member.year_start }}
									{% if member.cosupervisor %}
									<br>Co-supervisor: {{ member.cosupervisor }}
									{% endif %}
								</small>
							</p>
						</div>
						<div class="column is-full">
							<p class="is-size-7">
							<i>
								{{member.biography}}
							</i>
							</p>
						</div>
					</div>		
				</div>
			</div>
		  <footer class="card-footer" style="margin-top: auto;">
		  	<p class="card-footer-item">
					{{ member.project }}
					{% if member.project_url %}
						<a href="{{ site.baseurl }}/{{ member.project_url }}"><span class="tag is-light is-info">PDF</span></a>
					{% endif %}
				</p>
		  </footer>			
		</div>		
	</div>
	{% endfor %}
	</div>
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