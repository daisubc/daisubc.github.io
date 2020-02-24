---
layout: basic
title: News
permalink: /news/
---

<div class="content">
  <nav class="panel is-dark">
    {% for news in site.data.news %}
    <label class="panel-block" href="{{ news.url }}">
      <article class="media">
        <figure class="media-left">
          <p class="image is-64x64">
            {% if news.thumbnail %}
              <img src="{{ news.thumbnail }}">
            {% else %}
              <img src="https://bulma.io/images/placeholders/128x128.png">
            {% endif %}
          </p>
        </figure>
        <div class="media-content">
          <div class="content">
            <p>
              <small>{{ news.date | date_to_long_string}}</small>
              <br>
              <strong>{{ news.title }}</strong>
              <br>
              {{ news.description }}
            </p>
            <p>
              {% if news.url %}<b><a href="{{ news.url }}">[URL]</a></b>{% endif %}
            </p>
          </div>
        </div>
      </article>
    </label>
    {% endfor %}
  </nav>
</div>
