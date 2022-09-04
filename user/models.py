from django.db import models
from django.contrib.auth.models import User

class User(User):
    pass


class PlaceOwner(User):
    pass