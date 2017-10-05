# General
from webapp2 import WSGIApplication
from google.appengine.ext import db
from helpers import *


# Models
from models.user import User
from models.post import Post
from models.likes import Likes
from models.comment import Comment


# Handlers
from handlers.blog import BlogHandler
from handlers.blogfront import BlogFront
from handlers.signup import Signup
from handlers.login import Login
from handlers.logout import Logout
from handlers.post import PostPage
from handlers.newpost import NewPost
from handlers.editpost import EditPost
from handlers.deletepost import DeletePost
from handlers.likepost import LikePost
from handlers.newcomment import NewComment
from handlers.editcomment import EditComment
from handlers.deletecomment import DeleteComment
from handlers.welcome import Welcome


# Routing
app = WSGIApplication([
  ('/blog/?', BlogFront),
  ('/blog/([0-9]+)?', PostPage),
  ('/blog/newpost', NewPost),
  ('/blog/([0-9]+)/editpost', EditPost),
  ('/blog/([0-9]+)/deletepost/([0-9]+)', DeletePost),
  ('/blog/([0-9]+)/newcomment/([0-9]+)', NewComment),
  ('/blog/([0-9]+)/([0-9]+)/editcomment/([0-9]+)', EditComment),
  ('/blog/([0-9]+)/([0-9]+)/deletecomment/([0-9]+)', DeleteComment),
  ('/blog/([0-9]+)/like', LikePost),
  ('/signup', Signup),
  ('/login', Login),
  ('/logout', Logout),
  ('/welcome', Welcome)], debug=True)
