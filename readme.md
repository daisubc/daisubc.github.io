# UBC Data Analytics and Intelligent Systems Lab
<img src="./assets/img/dais_lab.png" width="250">

UBC DAIS - Data Analytics and Intelligent Systems Lab

- Lab Website: [https://dais.chbe.ubc.ca](https://dais.chbe.ubc.ca)
- Faculty Website: [https://chbe.ubc.ca/profile/bhushan-gopaluni/](https://chbe.ubc.ca/profile/bhushan-gopaluni/)

For current/incoming students: Please see below for a guide on updating this website.

---
  
### License
Copyright 2022 UBC DAIS Lab and [Bhushan Gopaluni](https://chbe.ubc.ca/profile/bhushan-gopaluni/). Website design and framework developed by [Siang Lim](https://www.siang.ca) in Jekyll/Liquid.

#### MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# New Students

## Account setup
1. Please create a GitHub account if you do not already have one. Send your GitHub username to `bhushan.gopaluni@ubc.ca` and CC `siang@alumni.ubc.ca` to add your account to the DAIS lab organization.
2. Wait for confirmation that your account has been added before proceeding.
3. You will receive an email from GitHub with an invitation to join the `daisubc` organization. Click accept. If you do not see the email, login to GitHub and check your notifications on the top right corner.

## Profile update
1. First, upload your profile pic to the [`assets/profile`](https://github.com/daisubc/daisubc.github.io/tree/master/assets/profile) folder. Important: Please crop your photo to a squarish shape and keep the file size to something reasonable, <1MB.
2. Then, create a new `.md` file with your name in the [`_profiles/`](https://github.com/daisubc/daisubc.github.io/tree/master/_profiles) folder. Use the existing profiles, an example is shown below for you to modify:

```
---
layout: biography
email: leeripp@chbe.ubc.ca
website: https://leerippon.com/
github: https://github.com/LeeRippon
project: Process Analytics and Machine Learning Techniques for the Kraft Pulping Process
img: leephoto2.png
degree: PhD
year_end: None
year_start: 2017
has_profile: True
biography: Lee Rippon is a PhD student studying Chemical and Biologial Engineering (CHBE) at UBC. He also holds BASc and MASc degrees from UBC in CHBE where his research experience includes applications of compressive sensing, adaptive control, system identification and process monitoring on sheet and film processes. His current research interests include applying process analytics and machine learning techniques to historical process data to perform fault detection, isolation, and diagnosis in a kraft pulping process.

cosupervisor: 
  - name: Philip Loewen (Math)
    url: https://www.math.ubc.ca/~loew/
title: Lee Rippon
pub_name: Lee D. Rippon
linkedin: https://www.linkedin.com/in/leerippon
---
```

# Main Settings

## Contact Information
Update your lab and contact information in the `_config.yml` file_

## Front page content
Edit `_includes/research.html` and `_layouts/home.html` to customize the front page

## General Layout Updates
To change the page layout, go to `/_includes` and edit the page partials. The default template can be changed in `_layouts`. Some pages can be edited directly in the markdown files contained in the root directory.

# Dynamic Content Updates

## Publications
Lab publications are displayed in each team member's profiles dynamically using the `team_profile_pubs.html` partial. The Liquid code loops through all papers in `site.data.publications` and displays the publication if the team member's `title` or `pub_name` variable, as configured in the `_profiles` folder, matches a name in the author list.

# Content Updates

## New News Articles
To update the news page with new articles, go to `/_news` and create a new markdown file. Use the existing articles as a template.

## New Publications
To update or add new entries to the publications page, go to `/_data/publications.yml`. Use the existing publications as a template.

## Group Members Page Update
1. Create a new `.md` file in the `/_profiles/` folder. Use the existing profiles as a template for the variable names.
2. Place your profile picture in the `/assets/profile` photo. Please crop your photo to a squarish shape and keep the filesize to something reasonable.

## Graduating Members
Graduating members are moved to `_data/alumni.yml`. The `status` variable in `_profiles` is set to `alumni` to disable the profile from being displayed in the teams page.
