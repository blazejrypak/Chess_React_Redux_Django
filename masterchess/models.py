# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models




class Game(models.Model):
    game_collation = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game_collation


class Move(models.Model):
    pos_from = models.IntegerField(null=True)
    pos_to = models.IntegerField(null=True)
    game = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
