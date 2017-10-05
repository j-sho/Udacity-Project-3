from google.appengine.ext import db


class Likes(db.Model):
    author = db.StringProperty()
    post_id = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user_id = db.IntegerProperty(required=True)
