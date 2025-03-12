from django.contrib.auth import get_user_model

class EmailBackend:
  def authenticate(self, request, username=None, password=None, **kwargs):
    UserModel = get_user_model()
    email = kwargs.get('email', username)
    try:
      user = UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
      return None
    else:
      if user.check_password(password):
        return user
    return None
  
  def get_user(self, user_id):
    UserModel = get_user_model()
    try:
      return UserModel.objects.get(pk=user_id)
    except UserModel.DoesNotExist:
      return None