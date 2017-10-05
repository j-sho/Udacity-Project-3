from google.appengine.ext import db
from handlers.blog import BlogHandler
from helpers import *
from models.user import User


class Welcome(BlogHandler):
    def get(self):
        if self.user:
            self.render('welcome.html', username=self.user.name)
        else:
            self.redirect('/signup')
