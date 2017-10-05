from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.comment import Comment


class NewComment(BlogHandler):
    def get(self, post_id, user_id):

        if self.user:
            self.render("comment.html")
        else:
            self.redirect('/login')

    def post(self, post_id, user_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())

        if not self.user:
            self.redirect('/login')

        content = self.request.get('content')
        author = self.user.name

        if content:
            c = Comment(parent=key, user_id=int(user_id),
                        content=content, author=author)
            c.put()
            self.redirect('/blog/' + post_id)
        else:
            error = "Write content, please!"
            self.render("comment.html", content=content, error=error)
