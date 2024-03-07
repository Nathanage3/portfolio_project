#!/usr/bin/python3
from flaskblog.models import Post
from flask_sqlalchemy import SQLAlchemy


posts = Post.query.all()

for post in posts:
  print(post)