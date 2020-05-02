# DAIS Website Guide

## News Update
To update the news page, go to `/_news`.

## Publications Update
To update the publications page, go to `/_data/publications.yml`.

## Group Members Page Update

- To update your project description that appears in the **People** page, go to the Members YAML file `/_data/members.yml` and update your `project` variable.

- If you'd like to attach a PDF link to your project, modify the `project_url` variable.

## Biography Page
To create an optional profile page

1. Create a new `.md` file in the `/_profiles/` folder. Use the existing profiles as a template for the variable names.
2. Place your profile picture in the `/assets/profile` photo. Please crop your photo to a squarish shape and keep the filesize to something reasonable.
3. Go to the members YAML file `/_data/members.yml` and then set the `has_profile` variable to `true`.
