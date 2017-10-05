from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *


class EditComment(BlogHandler):
    def get(self, post_id, post_user_id, comment_id):
        if self.user and self.user.key().id() == int(post_user_id):
            postKey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=postKey)
            comment = db.get(key)

            self.render('editcomment.html', content=comment.content)

        elif not self.user:
            self.redirect('/login')

        else:
            self.write("You don't have permission to edit this comment.")

    def post(self, post_id, post_user_id, comment_id):
        if self.request.get('save'):
            if not self.user:
                return

            if self.user and self.user.key().id() == int(post_user_id):
                content = self.request.get('content')

                postKey = db.Key.from_path('Post', int(post_id),
                                           parent=blog_key())
                key = db.Key.from_path('Comment', int(comment_id),
                                       parent=postKey)
                comment = db.get(key)

                comment.content = content
                comment.put()

                self.redirect('/blog/' + post_id)

            else:
                self.write("You don't have permission to edit this comment.")

        elif self.request.get('cancel'):
            return self.redirect('/blog/%s' % str(post_id))
