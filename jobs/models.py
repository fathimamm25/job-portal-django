from django.db import models

class Job(models.Model):
    employer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title