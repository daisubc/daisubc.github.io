---
layout: basic
title: News
permalink: /news/
---

{% assign articles = site.news | sort: 'date' | reverse %}

<div class="content">

<ol reversed class="list is-hoverable">
  {% for news in articles %}
  <li class="list-item" style="display: list-item">
    <p>
      <small>{{ news.date | date_to_long_string}}</small>
    <h5>
      <a href="{{ news.url }}"><strong>{{ news.title }}</strong></a>
    </h5>
      {{ news.content }}
    </p>
  </li>
  {% endfor %}
</ol>

</div>