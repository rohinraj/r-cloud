from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=100, default='Anonymous')
    def __str__(self):
        return self.file.name
