from .model import User


# Not work
class UserService:

    def __init__(self, username):
        self.user = User.objects.get(username=username)
