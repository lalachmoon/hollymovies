from django.contrib.auth.models import User
from django.db.models import CASCADE, Model, OneToOneField, TextField, BooleanField
from django.db import models


class Profile(Model):
    # OneToOne field insemna ca fiecare user este asociat cu un singur profil si vice-versa
    # on_delete CASCADE inseamna ca atunci cand stergem un user, se va sterge automat
    # si obiectul Profile asociat lui
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()



class AdminRequestMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_requests')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Câmp nou pentru aprobarea mesajului
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user.username} at {self.created_at}"