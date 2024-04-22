import pytest
from accounts.models import User


@pytest.mark.django_db
def test_user_creation():
  user = {'email': 'test@example.com', 'first_name' : 'test'}
  print ('the user count is ', User.objects.count())
  User.objects.create(**user)
  print ('the user count is ', User.objects.count())
