from typing import Optional

from django.contrib.auth.models import User

from account.models import Profile


def create_profile(backend, user, *args, **kwargs) -> None:
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:
    """
    Authenticate using an e-mail address
    """
    def authenticate(self, request, username: Optional[str] = None, password: Optional[str] = None) -> User | None:
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id: int) -> User | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
