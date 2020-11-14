# DAIS Website Guide
UBC DAIS Lab Website: [https://dais.chbe.ubc.ca](https://dais.chbe.ubc.ca)

Please see below for a guide on updating this website.

# Content Updates

## New News Articles
To update the news page with new articles, go to `/_news` and create a new markdown file. Use the existing articles as a template.

## New Publications
To update or add new entries to the publications page, go to `/_data/publications.yml`. Use the existing publications as a template.

## Group Members Page Update
1. Create a new `.md` file in the `/_profiles/` folder. Use the existing profiles as a template for the variable names.
2. Place your profile picture in the `/assets/profile` photo. Please crop your photo to a squarish shape and keep the filesize to something reasonable.
3. If you'd like to attach a PDF link to your project, modify the `project_url` variable.

# Layout Updates
To change the page layout, go to `/_includes` and edit the page partials. The default template can be changed in `_layouts`. Some pages can be edited directly in the markdown files contained in the root directory.
