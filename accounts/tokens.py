from datetime import date
from django.conf import settings
import uuid
from .models import Token

class PasswordResetTokenGenerator(object):
    """ A token generatore that fits PS1User needs
    """
    def make_token(self, user):
        t = Token(user)
        t.save()
        return str(t.key)

    def check_token(self, user, token):
        print("Token Check for %s, %s".format(user, token))
        t = Token.object.get(key=token)
        if t.user == user:
            return True
        return False

default_token_generator = PasswordResetTokenGenerator
