__author__ = 'abrange'

from .models import User


class EmailAuthBackend(object):
    """
    This Django Authentication Backend allow use email instead of user name to perform authentication.
    
    Usage:
    1) Include this file in your project, for example, same level as models.py
    2) Include this backend in your settings. Example:
        AUTHENTICATION_BACKENDS = (
        'fibase.email_authentication.EmailAuthBackend',
        'django.contrib.auth.backends.ModelBackend',
        ...
        )
        # Note: Here fibase is the name of my application, so you must change it to match your application folder

    """

    def authenticate(self, username=None, password=None):

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
