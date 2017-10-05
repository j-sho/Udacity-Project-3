from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.likes import Likes


class LikePost(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            self.write ("Sorry, you cannot like your own post.")
        elif not self.user:
            self.redirect('/login')
        else:
            user_id = self.user.key().id()
            post_id = post.key().id()
            author = self.user.name

            like = Likes.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            if like:
                self.redirect('/blog/' + str(post.key().id()))

            else:
                like = Likes(parent=key,
                            user_id=self.user.key().id(),
                            post_id=post.key().id())

                post.likes += 1

                like.put()
                post.put()

                self.redirect('/blog/' + str(post.key().id()))
