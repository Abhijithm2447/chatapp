from django.db import models

class IntentDB(models.Model):
    id = models.AutoField(primary_key=True)
    intent = models.CharField(max_length=250, unique=True)

class QueryDB(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.TextField()
    intent = models.ForeignKey(IntentDB, on_delete=models.CASCADE)