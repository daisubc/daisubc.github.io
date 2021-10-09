### {{ site.name }}

#### {{ site.jobtitle }}

[{{ site.department }}]({{ site.depturl }}){:target="_blank"}, {{ site.university }}

#### {{ site.secondjobtitle }}
[{{ site.faculty }}]({{ site.facultyurl }}){:target="_blank"}, {{ site.university }}

#### Faculty Profile
<a target="_blank" href="{{ site.facultyprofile }}"> {{ site.name }} </a>

#### Phone
{{ site.phone }}

#### Email
{% assign email = "bhushan.gopaluni@ubc.ca" | split: "@" %}
<a href="#" class="cryptedmail"
 data-name="{{ email[0] }}"
 data-domain="{{ email[1] }}"
 onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain; return false;">
</a>

#### Office
{{ site.office }}

#### Address
{{ site. address }}
{{ site. city }}, {{ site. region }} {{ site. postalcode }}