from tkinter import CASCADE
from django.db import models
from django.forms import CharField
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    stages = models.ManyToManyField('Stage',blank=False)


    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('Up','Up vote'),
        ('Down','Down vote'),
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    body = models.TextField(max_length=2000, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)    


    def __str__(self):
        return self.name


class Stage(models.Model):
    VOTE_TYPE = (
        ('Ongoing', 'Ongoing'),
        ('complete', 'Complete')
    )
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value