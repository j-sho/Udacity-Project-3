# Project Udacity Multi user blog
A simple multi user blog where:
- Users can sign in,
- Users can post blog posts,
- Users can edit/delete their posts,
- Users can comment on posts,
- Users can like posts, but not their own.

This project was developed as a part of the Udacity Full Stack Nanodegree program. It is built using and for Google App Engine.

# Files and directories
1) main.py - Imports handlers, houses the routing configurations and runs the webapp,
2) helpers.py - Contains functions to assist with primary application flow,
3) models - Directory with database model classes for facilitating database operations with Google Cloud Datastore:
- user.py - Contains User model class,
- post.py - Contains Post model class,
- comment.py - Contains Comment model class,
- like.py - Contains Like model class;
2) handlers - Directory contains handlers to handle each individual route:
- blogfront.py - Renders home page, showing 10 recent blogs posted by all users,
- blog.py - Handler provides to render multiple jinja templates with one handler,
- post.py - Displays a single post, and facilitates post comment creation,
- newpost.py - Renders form for writing a new post and saves post in database,
- welcome.py - Renders welcome form, 
- editpost.py - Database queries for edit user post,
- deletepost.py - Database queries for delete user post,
- login.py - Renders login form and validates usernames and passwords,
- logout.py - Clears authentication cookies,
- signup.py - Renders form for creating new users and saves data in database,
- newcomment.py - Renders form for creating new comment and saves data in database,
- editcomment.py - Database queries for edit user comment,
- deletecomment.py - Database queries for delete user comment,
- likepost.py - Database queries for save likes to posts.
3) static - Directory contains css style sheet and images folder.
4) templates - This folder contains all the html template files,
5) app.yaml - Has all the app configurations.

## How to Run
Make sure you have Google app engine installed

1. Clone the repository
2. cd into folder
3. spin up the server command `dev_appserver.py app.yaml`
4. Go to your browser and type [`http://localhost:8080`](http://localhost:8080)

## Front End
* Custom styles throush main.css

## Backend
* Python
* WebApp2 (Google appengine sdk)
