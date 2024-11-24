from django.contrib.auth.models import User
from django.db.models import CASCADE, Model, OneToOneField, TextField


class Profile(Model):
    # OneToOne field insemna ca fiecare user este asociat cu un singur profil si vice-versa
    # on_delete CASCADE inseamna ca atunci cand stergem un user, se va sterge automat
    # si obiectul Profile asociat lui
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()



