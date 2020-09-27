---
layout: basic
title: News
permalink: /news/
description: Latest news from the DAIS Lab research group at UBC. Check out our recent achievements and publications on process control, data analytics and machine learning.
---

{% assign articles = site.news | sort: 'date' | reverse %}

<div class="content">

<ol reversed class="list is-hoverable">
  {% for news in articles %}
  <li class="list-item" style="display: list-item" itemscope itemtype="http://schema.org/NewsArticle">
    <p>
      <small><time itemprop="datePublished" datetime="{{ news.date | date_to_xmlschema }}">{{news.date | date_to_long_string}}</time></small>
    <h5>
      <a href="{{ news.url }}"><strong itemprop="name headline">{{ news.title }}</strong></a>
    </h5>
    <div itemprop="articleBody">
      {{ news.content }}
    </div>
    </p>
  </li>
  {% endfor %}
</ol>

</div>