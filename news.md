---
layout: basic
title: News
permalink: /news/
description: Latest news from the DAIS Lab research group at UBC. Check out our recent achievements and publications on process control, data analytics and machine learning.
---

{% assign articles = site.news | sort: 'date' | reverse %}

<div class="content">

<ol reversed class="publist list-nomargin" style="list-style-position: inside;">
  {% for news in articles %}
  <li class="box box-left-border list-item" itemscope itemtype="http://schema.org/NewsArticle">
    <span class="news-date"><i>Posted: <time itemprop="datePublished" datetime="{{ news.date | date_to_xmlschema }}">{{news.date | date_to_long_string}}</time></i></span>
    <h5 class="news-title">
      <a href="{{ news.url }}"><strong itemprop="name headline">{{ news.title }}</strong></a>
    </h5>
    <div class="pub-news" itemprop="articleBody">
      <p>{{ news.content | strip_html | truncatewords: 30 }}</p>
    </div>
  </li>
  {% endfor %}
</ol>

</div>