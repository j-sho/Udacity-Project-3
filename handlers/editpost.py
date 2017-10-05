from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *


class EditPost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            self.render('editpost.html', subject=post.subject,
                        content=post.content, post_id=post_id)

        elif not self.user:
            self.redirect('/login')

        else:
            self.write("You have no permission edit this post.")

    def post(self, post_id):
        if self.request.get('save'):
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            if not self.user:
                return self.redirect('/login')

            if self.user and self.user.key().id() == post.user_id:
                subject = self.request.get('subject')
                content = self.request.get('content')
                author = self.user.name

                if subject and content:
                    key = db.Key.from_path('Post', int(post_id),
                                           parent=blog_key())
                    post = db.get(key)

                    post.subject = subject
                    post.content = content

                    post.put()

                    self.redirect('/blog/%s' % str(post.key().id()))
                else:
                    error = "Please provide subject and content!"
                    self.render("newpost.html", subject=subject,
                                content=content, error=error, author=author)

            else:
                self.write("You have no permission edit this post.")
        elif self.request.get('cancel'):
            return self.redirect('/blog/%s' % str(post_id))
