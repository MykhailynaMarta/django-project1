# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=username)  # Спочатку пробуємо знайти по email
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(username=username)  # Якщо не знайшли, шукаємо по username
            except UserModel.DoesNotExist:
                return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
